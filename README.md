# Covid-19_bot
Covid-19_bot - телеграм-бот для получения статистики по COVID19
## Запуск
```
python index.py
```
## Команды
Команды - способ способ коммуникации с ботом
### /start
Перенаправляет на /statistic
#### Ввод
```
/statistic
```
#### Вывод
```
Привет! Просмотреть статистику можно используя команду /statistic
```
### /statistic
Отправляет статистику по всему миру
#### Ввод
```
/statistic
```
#### Вывод
```
🌎 Весь мир

📊 5 090 166 случаев
🩹 65 816 767 тестов

🤒 2 734 983 +6 755 болеет
💊 2 025 444 +0 здоровых
💀 329 739 +500 смертей
```
### /regions
#### Ввод
```
/statistic > Азия > Китай
```
#### Вывод
```
🇨🇳 КНР

📊 82 967 случаев
🩹 0 тестов

🤒 84 +2 болеет
💊 78 249 +0 здоровых
💀 4 634 +0 смертей
```
```
🇹🇼 Тайвань

📊 447 случаев
🩹 17 200 тестов

🤒 35 +0 болеет
💊 411 +0 здоровых
💀 1 +0 смертей
```
## Зависимости
### COVID19 tracker
Поддержка api https://data.nepalcorona.info/api в python. [Подробнее](https://github.com/jDan735/covid19-tracker)
