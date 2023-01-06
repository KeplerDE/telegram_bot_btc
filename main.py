import requests
from datetime import datetime
import telebot
from auth_data import token

def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")    # получаем дату и стоимость

def telegram_bot(token):
    bot = telebot.TeleBot(token)        # создали бота

    @bot.message_handler(commands=["start"])         # сообщение приветствия
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! Write the 'price' to find out the cost of BTC!")  # первое кому, второе что отправить


    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":                 # если текст сообщения равен
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")   # то в ответ уходит курс
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn...Something was wrong..."
                )
        else:
            bot.send_message(message.chat.id, "Whaaat??? Check the command dude!")

    bot.polling()    # проверяет есть ли новые сообщения


# бот готов, теперь нужно использовать PuTTY для win для установки SSH и можно заливать на VPS
if __name__ == '__main__':
    # get_data()
    telegram_bot(token)
