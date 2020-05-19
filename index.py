import telebot
import COVID19Py
import json
import sys
import time

sys.path.insert(0, "./lib")
import lib
import covid19

with open("./botdata/countries.json", "r", encoding="utf-8") as datafile:
    data = json.loads(datafile.read())

with open("./botdata/token.txt") as token:
    bot = telebot.TeleBot(token.read())

def getPrettyNumber(number):
    return str((f"{number:,}").replace(",", " "))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Просмотреть статистику можно используя команду /statistic')

@bot.message_handler(commands=["statistic"])
def send_statistic(message):
    world = covid19.getWorld()
    bot.send_message(message.chat.id, "🌎 *Весь мир*\n\n" + 
        "📊 *" + lib.getPrettyNumber(world["cases"]) + "* случаев\n" +
        "🩹 *" + lib.getPrettyNumber(world["tests"]) + "* тестов\n\n" +
        "🤒 *" + lib.getPrettyNumber(world["active"]) + "* `+" + lib.getPrettyNumber(world["todayCases"]) + "` болеет\n" +
        "💊 *" + lib.getPrettyNumber(world["recovered"]) + "* `+" + "0" + "` здоровых\n" +
        "💀 *" + lib.getPrettyNumber(world["deaths"]) + "* `+" + lib.getPrettyNumber(world["todayDeaths"]) + "` смертей",
        parse_mode = "Markdown")

def loadMenu (info, message, text):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for item in info:
        keyboard.add(telebot.types.InlineKeyboardButton(text=item[0], callback_data=item[0]))
    bot.send_message(message.from_user.id, text=text, reply_markup=keyboard)
    
def loadMenuFromCall (info, message, text):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for item in info:
        keyboard.add(telebot.types.InlineKeyboardButton(text=item[0], callback_data=item[0]))
    bot.send_message(message.chat.id, text=text, reply_markup=keyboard)

@bot.message_handler(commands=["regions"])
def getOurRegion (message):

    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(telebot.types.InlineKeyboardButton(text="Азия", callback_data="asia"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Америка", callback_data="america"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Африка", callback_data="africa"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Океания", callback_data="oceania"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Европа", callback_data="europa"))

    bot.send_message(message.from_user.id, text = "Выберите часть света", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.delete_message(call.from_user.id, call.message.message_id)

    # ===== Asia =====

    if call.data == "asia":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Китай", callback_data="china"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Остальное", callback_data="asia_rest"))
        bot.send_message(call.message.chat.id, text = "Выберите регион", reply_markup = keyboard)
    if call.data == "china":
        data2 = covid19.getCountries()
        for country in data[0][1][0][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)
    if call.data == "asia_rest":
        data2 = covid19.getCountries()
        for country in data[0][1][1][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)

    # ===== America =====

    if call.data == "america":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Северная Америка", callback_data="north_america"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Южная Америка", callback_data="south_america"))
        bot.send_message(call.message.chat.id, text = "Выберите регион", reply_markup = keyboard)
    if call.data == "north_america":
        data2 = covid19.getCountries()
        for country in data[1][1][0][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)  
    if call.data == "south_america":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Карибские страны", callback_data="caribian"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Остальные страны", callback_data="south_america_rest"))
        bot.send_message(call.message.chat.id, text = "Выберите регион", reply_markup = keyboard)  
    if call.data == "caribian":
        data2 = covid19.getCountries()
        for country in data[1][1][1][1][0][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)
    if call.data == "south_america_rest":
        data2 = covid19.getCountries()
        for country in data[1][1][1][1][1][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country) 

    # ===== Africa [beta] =====

    if call.data == "africa":
        data2 = covid19.getCountries()
        for country in data[2][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country) 

    # ===== Oceania =====

    if call.data == "oceania":
        data2 = covid19.getCountries()
        for country in data[3][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)     

    # ===== Europa =====

    if call.data == "europa":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Евросоюз", callback_data="EU"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="СНГ", callback_data="CIS"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Остальные", callback_data="europa_rest"))
        bot.send_message(call.message.chat.id, text = "Выберите регион", reply_markup = keyboard)    

    if call.data == "CIS":
        data2 = covid19.getCountries()
        for country in data[4][1][0][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)

    if call.data == "europa_rest":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Югославия", callback_data="yugoslavia"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Остальные", callback_data="europa_rest_rest"))
        bot.send_message(call.message.chat.id, text = "Выберите регион", reply_markup = keyboard) 
    if call.data == "yugoslavia":
        data2 = covid19.getCountries()
        for country in data[4][1][1][1][0][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)
    if call.data == "europa_rest_rest":
        data2 = covid19.getCountries()
        for country in data[4][1][1][1][1][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)

    if call.data == "EU":
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Чехословакия", callback_data="czech"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Бенилюкс", callback_data="benilux"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Прибалтика", callback_data="pribaltica"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Балканы", callback_data="balcans"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Скандинавия", callback_data="scandinavia"))
        keyboard.add(telebot.types.InlineKeyboardButton(text="Остальные", callback_data="eu_rest"))
        bot.send_message(call.message.chat.id, text = "Выберите регион", reply_markup = keyboard) 

    if call.data == "czech":
        data2 = covid19.getCountries()
        for country in data[4][1][2][1][0][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)

    if call.data == "benilux":
        data2 = covid19.getCountries()
        for country in data[4][1][2][1][1][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)

    if call.data == "pribaltica":
        data2 = covid19.getCountries()
        for country in data[4][1][2][1][2][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)

    if call.data == "balcans":
        data2 = covid19.getCountries()
        for country in data[4][1][2][1][5][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)


    if call.data == "scandinavia":
        data2 = covid19.getCountries()
        for country in data[4][1][2][1][3][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)

    if call.data == "eu_rest":
        data2 = covid19.getCountries()
        for country in data[4][1][2][1][4][1]:
            data1 = data2[country[1]]
            lib.sendLocationStatsFromCall(call, data2[country[1]], country)

@bot.message_handler(commands=["time"])
def sendStats (message):
    bot.send_message(message.chat.id, message.text.replace("/time ", ""))

bot.polling()
