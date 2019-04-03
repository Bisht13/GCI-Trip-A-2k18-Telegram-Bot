import telebot
import datetime
import time
from datetime import datetime
import os

bot = telebot.TeleBot(token=os.environ['SUPERIOR_TELEGRAM_BOT_API'])

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Welcome!')

@bot.message_handler(commands=['Instagram'])
def send_welcome(message):
    bot.reply_to(message,'Enter username with id @')
    
@bot.message_handler(commands=['repo'])
def send_welcome(message):
    bot.reply_to(message,'https://github.com/Bisht13/GCI-Trip-A-2k18-Telegram-Bot')

@bot.message_handler(func= lambda msg: msg.text is not None and '@' in msg.text and 'id' in msg.text)
def at_answer(message):
    texts = message.text.split()
    id = find_at(texts)
    bot.reply_to(message, 'https://instagram.com/{}'.format(id[1:]))

@bot.message_handler(commands=['countdown'])
def send_welcome(message):
    reqdate = datetime(2019, 6, 9, 0, 0, 0)
    diff = reqdate - datetime.utcnow()
    (d, t) = str(diff).split(',')
    (h, m, s) = str(t).split(':')
    s = int(round(float(s)))
    bot.reply_to(message, d + ' ' + str(h) + " hours " + str(m) + " minutes " + str(s) + " seconds remaining")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

