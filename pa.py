import calendar
from datetime import date
import requests
import json
from configparser import ConfigParser
import keyboard

hotkey = "ctrl + x"

remind = open("reminders.txt")

today = date.today()
month = today.month
year = today.year
calendar = calendar.month(year,month)
ascii_art = open("ascii_art")
print(ascii_art.read())
print("Options: ")
print("Calendar:\tc\t\tLeave Inputs:\tctrl + x")
print("Weather:\tw")
print("Reminder:\tr")
print("Summary:\tsum")
print("Search: \tsearch")
print("Close PA:\tstop")
print("\n")
pa = "a"
while pa == "c" or "w" or "r" or "s" or "search":
    pa = (input("How may I be of assistance? "))
    if pa == "c":
        print("\n")
        print("Today: ", today)
        print(calendar)

    elif pa == "w":
        try:
            config_object = ConfigParser()
            config_object.read("config.ini")
            weather_api_key = config_object['weather_api_key']
            city_lat = config_object['city_lat']
            city_lon = config_object['city_lon']
            api_key = weather_api_key["api_key"]
            lat = city_lat["lat"]
            lon = city_lon["lon"]
            Final_url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
            weather_data = requests.get(Final_url).json()
            temp = weather_data["current"]["temp"]
            print("current temp: ", temp)
        except KeyError:
            print("Please add OpenWeather api-key, latitude, and longitude to config.ini")
            continue

    elif pa == "r":
        remind.seek(0)
        print(remind.read())
        reminder = (input("\nadd:\t+\nremove:\t-\nWhat would you like to do? "))
        if reminder == "+":
            remind = open("reminders.txt" , "a")
            remind.write("\n")
            remind.write(input("add reminder: "))
            remind.close()
            remind = open("reminders.txt", "a+")
            remind.seek(0)
            print(remind.read())
            if keyboard.is_pressed(hotkey):
                break
            continue

        elif reminder == "-":
            fn = 'reminders.txt'
            f = open(fn)
            output = []
            str = input("first word/words of reminder: ")
            for line in f:
                if not line.startswith(str):
                    output.append(line)
            f.close()
            f = open(fn, 'w')
            f.writelines(output)
            f.close()
            remind.seek(0)
            print(remind.read())
            if keyboard.is_pressed(hotkey):
                break
        else:
            break

    elif pa == "sum":
        remind.seek(0)
        print(remind.read())
        print("Today: ", today)
        print(calendar)
        try:
            config_object = ConfigParser()
            config_object.read("config.ini")
            weather_api_key = config_object['weather_api_key']
            city_lat = config_object['city_lat']
            city_lon = config_object['city_lon']
            api_key = weather_api_key["api_key"]
            lat = city_lat["lat"]
            lon = city_lon["lon"]
            Final_url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
            weather_data = requests.get(Final_url).json()
            temp = weather_data["current"]["temp"]
            print("current temp: ", temp)
        except KeyError:
            print("Please complete weather parameters.")

    elif pa == "search":
        from urllib.request import urlretrieve
        from urllib.parse import quote
        import webbrowser
        query = quote(input("Search: "))
        search = webbrowser.open("https://duckduckgo.com/?q=" + query)
        if keyboard.is_pressed(hotkey):
            break
        continue

    elif pa == "stop":
        print("Goodbye!")
        break

    else:
        print("Please Re-state")
