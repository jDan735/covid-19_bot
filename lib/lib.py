import telebot
import json

with open("./botdata/token.txt") as token:
    bot = telebot.TeleBot(token.read())

def getPrettyNumber(number):
	return str((f"{number:,}").replace(",", " "))

def sendLocationStats(message, data, country):
    bot.send_message(call.message.chat.id, country[2] + "* " + country[0] + "*\n\n" +
        "📊 *" + getPrettyNumber(data["totalCases"]) + "* случаев\n" +
        "🩹 *" + getPrettyNumber(data["tests"]) + "* тестов\n\n" +
        "🤒 *" + getPrettyNumber(data["activeCases"]) + "* `+" + getPrettyNumber(data["newCases"]) + "` болеет\n" +
        "💊 *" + getPrettyNumber(data["totalRecovered"]) + "* `+" + "0" + "` здоровых\n" +
        "💀 *" + getPrettyNumber(data["totalDeaths"]) + "* `+" + getPrettyNumber(data["newDeaths"]) + "` смертей",
        parse_mode = "Markdown")