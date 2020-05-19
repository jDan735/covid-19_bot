import telebot
from telebot import types
import COVID19Py
import json


token = open("./botdata/token.txt", "r")
bot = telebot.TeleBot(token.read())
token.close()

with open("countries.json", "r", encoding="utf-8") as datafile:
    data = json.loads(datafile.read())


covid19 = COVID19Py.COVID19()
latest = covid19.getLatest()

def getPrettyNumber(number):
	return str((f"{number:,}").replace(",", " "))

def getCountryLatestData (countryid):
	if str(type(countryid)) == "<class 'int'>":
		country = covid19.getLocationById(countryid)
	elif str(type(countryid)) == "<class 'str'>":
		countryplaces = covid19.getLocationByCountryCode(countryid)
		country = {
			"new": {
				"confirmed": 0,
				"deaths": 0
			},
			"old": {
				"confirmed": 0,
				"deaths": 0
			}
		}
		for place in countryplaces:
			country["new"]["confirmed"] += place["latest"]["confirmed"]
			country["new"]["deaths"] += place["latest"]["deaths"]
	return {
		"old": {
			"confirmed": str(getPrettyNumber(country["latest"]["confirmed"] - country["timelines"]["confirmed"]["timeline"]["2020-05-14T00:00:00Z"])),
			"deaths": str(getPrettyNumber(country["latest"]["deaths"] - country["timelines"]["deaths"]["timeline"]["2020-05-14T00:00:00Z"]))		
		},
		"new": {
			"confirmed": str(getPrettyNumber(country["latest"]["confirmed"])),
			"deaths": str(getPrettyNumber(country["latest"]["deaths"]))
		}
	}

def sendLocationStatsFromCall(call, data, country):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(text="Подробнее", callback_data="more"))

def sendLocationStatsFromCall(call, data, country):
    bot.send_message(call.message.chat.id, country[2] + "* " + country[0] + "*\n\n" +
        "📊 *" + getPrettyNumber(data["totalCases"]) + "* случаев\n" +
        "🩹 *" + getPrettyNumber(data["tests"]) + "* тестов\n\n" +
        "🤒 *" + getPrettyNumber(data["activeCases"]) + "* `+" + getPrettyNumber(data["newCases"]) + "` болеет\n" +
        "💊 *" + getPrettyNumber(data["totalRecovered"]) + "* `+" + "0" + "` здоровых\n" +
        "💀 *" + getPrettyNumber(data["totalDeaths"]) + "* `+" + getPrettyNumber(data["newDeaths"]) + "` смертей",
        parse_mode = "Markdown")
    
def sendLocationStats(message, data, country):
    bot.send_message(call.message.chat.id, country[2] + "* " + country[0] + "*\n\n" +
        "📊 *" + getPrettyNumber(data["totalCases"]) + "* случаев\n" +
        "🩹 *" + getPrettyNumber(data["tests"]) + "* тестов\n\n" +
        "🤒 *" + getPrettyNumber(data["activeCases"]) + "* `+" + getPrettyNumber(data["newCases"]) + "` болеет\n" +
        "💊 *" + getPrettyNumber(data["totalRecovered"]) + "* `+" + "0" + "` здоровых\n" +
        "💀 *" + getPrettyNumber(data["totalDeaths"]) + "* `+" + getPrettyNumber(data["newDeaths"]) + "` смертей",
        parse_mode = "Markdown")
