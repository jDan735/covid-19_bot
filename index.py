import telebot
import COVID19Py

locale = "ru"

token = open("token.txt", "r")
bot = telebot.TeleBot(token.read())
print(token.read())
token.close()

covid19 = COVID19Py.COVID19()
latest = covid19.getLatest()

num1 = latest["confirmed"]
num2 = latest["deaths"]

num3 = f"{num1:,}"
num4 = f"{num2:,}"

num5 = num3.replace(",", " ")
num6 = num4.replace(",", " ")



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Просмотреть статистику можно используя команду /statistic')

@bot.message_handler(commands=["statistic"])
def send_statistic(message):
	bot.send_message(message.chat.id, "🌎")
	bot.send_message(message.chat.id, "*Весь мир:*\n\n🦠 *" + num5 + "* заражённых \n💀 *" + num6 + "* умерших \n🗺 *" + "185" + "* регионов", parse_mode="Markdown")















ua = covid19.getLocationByCountryCode("UA")[0]["latest"]
num_ua1 = ua["confirmed"]
num_ua2 = ua["deaths"]

num_ua3 = f"{num_ua1:,}"
num_ua4 = f"{num_ua2:,}"

num_ua5 = num_ua3.replace(",", " ")
num_ua6 = num_ua4.replace(",", " ")

@bot.message_handler(commands=["ua"])
def send_statistic_ua(message):
	bot.send_message(message.chat.id, "🇺🇦")
	bot.send_message(message.chat.id, '*Украина:*\n\n🦠 *' + num_ua5 + "* заражённых \n💀 *" + num_ua6 + "* умерших", parse_mode="Markdown")

bot.polling()
