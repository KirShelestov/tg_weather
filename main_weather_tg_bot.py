import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hello! Send me city's name and I'll send broadcast")
@dp.message_handler()
async def get_weather(message: types.Message):
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
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
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
        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%n=%d %H:%M')}***\n"
            f"Weather's in city: {city}\nTemperature: {cur_weather}°C {wd}\n"
              f"Humidity: {humidity}\nPressure: {pressure}mm\nWind: {wind}\n"
              f"Sunrise: {sunrise}\n"
              f"Sunset: {sunset}\n"
              f"Length of day: {length_of_day}\n"
              f"Have a good day!"
              )
        

    except:
        await message.reply("Check city's name,please")

if __name__ == '__main__':
    executor.start_polling(dp)