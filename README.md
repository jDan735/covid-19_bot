# 🤖 Covid-19_bot
Covid-19_bot - telegram-bot for statistics on COVID19
## 🚀 Start
```
python index.py
```
## 🎛 Commands
### /start
Link to /statistic
#### 📥 Input
```
/statistic
```
#### 📤 Output
```
Привет! Просмотреть статистику можно используя команду /statistic
```
### /statistic
Send world statistic
#### 📥 Input
```
/statistic
```
#### 📤 Output
```
🌎 Весь мир

📊 5 090 166 случаев
🩹 65 816 767 тестов

🤒 2 734 983 +6 755 болеет
💊 2 025 444 +0 здоровых
💀 329 739 +500 смертей
```
### /regions
Send region statistic
#### 📥 Input
```
/statistic > Азия > Китай
```
#### 📤 Output
```
🇨🇳 КНР

📊 82 967 случаев
🩹 0 тестов

🤒 84 +2 болеет
💊 78 249 +0 здоровых
💀 4 634 +0 смертей

...
```
## 🔨 Dependencies
### 📢 [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
### 👑 [COVID19 tracker](https://github.com/jDan735/covid19-tracker)
