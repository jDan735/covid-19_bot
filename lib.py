import telebot
from telebot import types
import COVID19Py
import json


token = open("./botdata/token.txt", "r")
bot = telebot.TeleBot(token.read())
token.close()

datafile = open("countries.json", "r", encoding="utf-8")
data = json.loads(datafile.read())
datafile.close()


covid19 = COVID19Py.COVID19()
latest = covid19.getLatest()

menufile = open("./botdata/menu.json", "r", encoding="utf-8")
menu = json.loads(menufile.read())
menufile.close()

def getCountryLatestData (countryid):
	if str(type(countryid)) == "<class 'int'>":
		country = covid19.getLocationById(countryid)["latest"]
	elif str(type(countryid)) == "<class 'str'>":
		countryplaces = covid19.getLocationByCountryCode(countryid)
		country = {"confirmed": 0, "deaths": 0}
		for place in countryplaces:
			country["confirmed"] += place["latest"]["confirmed"]
			country["deaths"] += place["latest"]["deaths"]

	num_country1 = country["confirmed"]
	num_country2 = country["deaths"]

	num_country3 = f"{num_country1:,}"
	num_country4 = f"{num_country2:,}"

	num_country5 = num_country3.replace(",", " ")
	num_country6 = num_country4.replace(",", " ")

	return {
		"confirmed": num_country5,
		"deaths": num_country6
	}

def loadMenu (message, text):
	keyboard = types.InlineKeyboardMarkup()
	for item in menu:
		keyboard.add(types.InlineKeyboardButton(text=item[0], callback_data=item[0]))
	bot.send_message(message.from_user.id, text=text, reply_markup=keyboard)



	



