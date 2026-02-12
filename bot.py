import telebot
import requests

BOT_TOKEN = "Enter bot's API_KEY from Bot Father"
WEATHER_API_KEY = "Take API)KEY from the site"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! 🌤\nНапиши название города, и я покажу погоду."
    )

@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city = message.text

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        weather_message = (
            f"🌍 Город: {city}\n"
            f"🌡 Температура: {temperature}°C\n"
            f"☁ Погода: {description}\n"
            f"💧 Влажность: {humidity}%"
        )

        bot.send_message(message.chat.id, weather_message)

    else:
        bot.send_message(
            message.chat.id,
            "❌ Город не найден. Попробуй ещё раз."
        )


bot.polling(none_stop=True)
