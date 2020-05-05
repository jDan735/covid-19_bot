import telebot
from telebot import types
import COVID19Py
import json
import sys

sys.path.insert(0, ".")
import lib

token = open("./botdata/token.txt", "r")
bot = telebot.TeleBot(token.read())
token.close()

menufile = open("./botdata/menu.json", "r", encoding="utf-8")
menu = json.loads(menufile.read())
menufile.close()

datafile = open("countries.json", "r", encoding="utf-8")
data = json.loads(datafile.read())
datafile.close()

covid19 = COVID19Py.COVID19()
latest = covid19.getLatest()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Просмотреть статистику можно используя команду /statistic')

@bot.message_handler(commands=["statistic"])
def send_statistic(message):
    num1 = latest["confirmed"]
    num2 = latest["deaths"]

    num3 = f"{num1:,}"
    num4 = f"{num2:,}"

    num5 = num3.replace(",", " ")
    num6 = num4.replace(",", " ")

    bot.send_message(message.chat.id, "🌎 *Весь мир:*\n\n🦠 *" + num5 + "* заражённых \n💀 *" + num6 + "* умерших \n🗺 *" + "185" + "* регионов", parse_mode="Markdown")
        
@bot.message_handler(commands=["regions"])
def getOurRegion (message):
    lib.loadMenu(message, "Выберите регион")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.delete_message(call.from_user.id, call.message.message_id)
    for item in menu["region-choice-menu"]:
        if call.data == item[0]:
            for key in data:
                if key["name"].lower() == item[0].lower():
                    for i in key["contries"]:
                        data_local = lib.getCountryLatestData(i["id"])
                        bot.send_message(call.message.chat.id, i["emoji"] + ' *' + i["name"] + ":*\n\n🦠 *" + data_local["confirmed"] + "* заражённых \n💀 *" + data_local["deaths"] + "* умерших", parse_mode="Markdown")
            break

@bot.message_handler(commands=["time"])
def sendStats (message):
    bot.send_message(message.chat.id, message.text.replace("/time ", ""))

bot.polling()
