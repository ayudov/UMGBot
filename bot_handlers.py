from bot import bot
from buttons import *
from db import *
from datetime import datetime
import pandas as pd
import requests
import config
import io


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not User.objects(user_id=message.from_user.id):
        User(user_id=message.from_user.id, Name=str(message.from_user.username), state='start', Reg_time=datetime.utcnow()).save()
        bot.send_message(message.chat.id, HELLO_MESSAGE)
    else: bot.send_message(message.chat.id, HELLO_AGAIN_MESSAGE)


@bot.message_handler(content_types=['document'])
def handle_docs_audio(message):
    print(message.document)
    file_info = bot.get_file(message.document.file_id)
    file_url = 'https://api.telegram.org/file/bot'+str(config.TOKEN)+'/'+str(file_info.file_path)
    xl = pd.ExcelFile(file_url)
    print(xl.sheet_names)
    df1 = xl.parse('Sosi')
    print(df1)


if __name__ == '__main__':
    bot.polling(none_stop=True)
