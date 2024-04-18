import requests
import datetime
from pprint import pprint

from config import open_weather_token

def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B",

    }
    try:
        r = requests.get (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        
        data = r.json()
        #pprint(data)
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        weather_discript = data["weather"][0]["main"]

        if weather_discript in code_to_smile:
            wd = code_to_smile[weather_discript]
        else:
            wd = "Look through window"

        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        print(f"***{datetime.datetime.now().strftime('%Y-%n=%d %H:%M')}***\n"
            f"Weather's in city: {city}\nTemperature: {cur_weather}°C {wd}\n"
              f"Humidity: {humidity}\nPressure: {pressure}mm\nWind: {wind}\n"
              f"Sunrise: {sunrise}\n"
              f"Sunset: {sunset}\n"
              f"Length of day: {length_of_day}\n"
              f"Have a good day!"
              )
        

    except Exception as ex:
        print(ex)
        print("Check city's name,please")

def main():
    city = input("City:")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
