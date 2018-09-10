
from bot import bot
from buttons import *
from db import db


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)




if __name__ == '__main__':
    bot.polling(none_stop=True)
