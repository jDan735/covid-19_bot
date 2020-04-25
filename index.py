import telebot
import COVID19Py
import json

token = open("token.txt", "r")
bot = telebot.TeleBot(token.read())
token.close()

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

    bot.send_message(message.chat.id, "🌎")
    bot.send_message(message.chat.id, "*Весь мир:*\n\n🦠 *" + num5 + "* заражённых \n💀 *" + num6 + "* умерших \n🗺 *" + "185" + "* регионов", parse_mode="Markdown")






def getCountryLatestData (countryid):
    country = covid19.getLocationByCountryCode(countryid)[0]["latest"]

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

@bot.message_handler(content_types=["text"])
def getRegionLatest (message):
    region_finded = False
    for key in data:
        if key["name"].lower() == message.text.lower():
            region_finded = True
            for i in key["contries"]:
                data_local = getCountryLatestData(i["id"])

                bot.send_message(message.chat.id, i["emoji"])
                bot.send_message(message.chat.id, '*' + i["name"] + ":*\n\n🦠 *" + data_local["confirmed"] + "* заражённых \n💀 *" + data_local["deaths"] + "* умерших", parse_mode="Markdown")


    if region_finded == False:
        bot.send_message(message.chat.id, "Данный регион не существует, попробуйте ввести его название снова")



bot.polling()
