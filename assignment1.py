
import requests
import pandas as pd

data = requests.get(
    "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")


jsondata = dict(data.json())
listdata = (list(jsondata["list"]))

df = pd.DataFrame(listdata)
df.set_index("dt_txt", inplace=True)


while (True):
    print("""
    1 -> Get temperature 
    2 -> Get wind speed
    3 -> Get pressure
    4 -> exit
    """)
    i = int(input("Enter option:"))
    if i == 4:
        break
    elif (i > 0 and i < 4):
        dt = str(input("Enter the date and time in the formart YYYY/MM/DD HH:MM:SS "))
        try:
            d = dict(df.loc[dt])
        except KeyError:
            print("The date time not found")

        if i == 1:
            print(d['main']['temp'])
        elif i == 2:
            print(d['wind']['speed'])
        elif i == 3:
            print(d['main']['pressure'])
    else:
        print("enter one of the inputs")
