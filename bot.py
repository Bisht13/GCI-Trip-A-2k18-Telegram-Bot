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

def find_exclaimation(msg):
    for text in msg:
        if '!' in text:
            return text

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Welcome!')

@bot.message_handler(commands=['Instagram'])
def send_Instagram_Message(message):
    bot.reply_to(message,'Enter username with id @')

@bot.message_handler(commands=['repo'])
def send_Repo_URL(message):
    bot.reply_to(message,'https://github.com/Bisht13/GCI-Trip-A-2k18-Telegram-Bot')

@bot.message_handler(func= lambda msg: msg.text is not None and '@' in msg.text and 'id' in msg.text)
def send_Instgram_ID(message):
    texts = message.text.split()
    id = find_at(texts)
    bot.reply_to(message, 'https://instagram.com/{}'.format(id[1:]))

@bot.message_handler(commands=['countdown'])
def send_Countdown(message):
    reqdate = datetime(2019, 6, 9, 0, 0, 0)
    diff = reqdate - datetime.utcnow()
    (d, t) = str(diff).split(',')
    (h, m, s) = str(t).split(':')
    s = int(round(float(s)))
    bot.reply_to(message, d + ' ' + str(h) + " hours " + str(m) + " minutes " + str(s) + " seconds remaining")

@bot.message_handler(commands=['ResetInstaIDs'])
def reset_IDs():
    instaIDs = open('instaIDs.txt','w+')
    instaIDs.write('')

@bot.message_handler(commands=['InstaAdd'])
def reply_to_add_ID(message):
    bot.reply_to(message,'To add your ID to /Insta list. Please write in the format given below \n !Yourname @YourID')

@bot.message_handler(func= lambda msg: msg.text is not None and '!' in msg.text and '@' in msg.text)
def add_ID(message):
    texts = message.text.split()
    name = find_exclaimation(texts)[1:]
    id = find_at(texts)[1:]
    instaIDs = open('instaIDs.txt','a+')
    instaIDs.write(name + '   @' + id + '\n')
    bot.reply_to(message, 'Your ID has been add :D')

@bot.message_handler(commands=['InstaIDs'])
def send_insta_ids(message):
    instaID = open('instaIDs.txt','r')
    if instaID.mode == 'r':
        bot.reply_to(message, instaID.read())

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
