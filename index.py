import telebot
from telebot import types
import COVID19Py
import json
import sys
import time

sys.path.insert(0, ".")
import lib

with open("countries.json", "r", encoding="utf-8") as datafile:
    data = json.loads(datafile.read())

with open("./botdata/token.txt") as token:
    bot = telebot.TeleBot(token.read())

covid19 = COVID19Py.COVID19()
changes = covid19.getLatestChanges()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Просмотреть статистику можно используя команду /statistic')

@bot.message_handler(commands=["statistic"])
def send_statistic(message):
    latest = covid19.getLatest()
    data = covid19.getAll(timelines=True)

    old = {
        "confirmed": 0,
        "deaths": 0
    }
    i = 0
    while i != 256:
        place = data["locations"][i]
        old["confirmed"] += place["timelines"]["confirmed"]["timeline"]["2020-05-14T00:00:00Z"]
        old["deaths"] += place["timelines"]["deaths"]["timeline"]["2020-05-14T00:00:00Z"]
        i += 1
    old = {
        "confirmed": lib.getPrettyNumber(latest["confirmed"] - old["confirmed"]),
        "deaths": lib.getPrettyNumber(latest["deaths"] - old["deaths"])
    }
    new = {
        "confirmed": lib.getPrettyNumber(latest["confirmed"]),
        "deaths": lib.getPrettyNumber(latest["deaths"])        
    }
    bot.send_message(message.chat.id, "🌎 *Весь мир:*\n\n🦠 *" + new["confirmed"] + "* `+" + old["confirmed"] + "` заражённых \n💀 *" + new["deaths"] + "* `+" + old["deaths"] + "` умерших", parse_mode="Markdown")

@bot.message_handler(commands=["regions"])
def getOurRegion (message):
    lib.loadMenu(data, message, "Выберите часть света")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.delete_message(call.from_user.id, call.message.message_id)
    for item in data:
        if call.data == item[0]:
            if type(item[1][0][1]) == list:
                lib.loadMenuFromCall(item[1], call.message, "Выберите регион")
            elif type(item[1][0][2]) == str:
                for country in item[1]:
                    data_local = lib.getCountryLatestData(country[1])
                    bot.send_message(call.message.chat.id, country[2] + " *" + country[0] + ":*\n\n🦠 *" + data_local["new"]["confirmed"] + "* `+" + data_local["old"]["confirmed"] + "` заражённых \n💀 *" + data_local["new"]["deaths"] + "* `+" + data_local["old"]["deaths"] + "` умерших", parse_mode="Markdown")


@bot.message_handler(commands=["time"])
def sendStats (message):
    bot.send_message(message.chat.id, message.text.replace("/time ", ""))

bot.polling()
