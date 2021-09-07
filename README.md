<div align="center">
    <img src="https://download.logo.wine/logo/Binance/Binance-Logo.wine.png" height="300">
</div>

# Getting Started
Binance trade bot does automatic buy and sell operations.It try to make profit even you don't need to look to the stock market. Indicators that we use for this project make profit for you. If decrease %1,5 of coin value that we buy, it will sell the coin (You can change the percent).

### Prerequisites
- Python 3.x.x
- numpy
- pandas
- talib
- binance api
- telebot
- bs4
- selenium
- threading
- Telebot token via website

### Installing
- This bot send messages for every buy or sell action. It is presumed that you have obtained an **API token with @BotFather**. We will call this token TOKEN. You need to write your TOKEN to the **Bot_Token** variable. And after you create a telegram group, you need to get its **Chat_ID** and write it to Chat_ID variable section.
- You need to get your **Binance key and secret** key for access your account for buy and sell actions. And write your **KEY and SECRET** on lines 89 and 90.
- Then you need to install the necessary libraries,then you can be run on the command line with the python bot.py command.

### How It Works
This bot search all coins that we define (also you can add more). At the same time it check indicators that we coded for every coin. If it find perfect combination of indicators, then it buy the coin. This programme just you your BTC balance and it split your money for 5 coin. After buy 5 coin it check situation of this coins for every second. Meanwhile a chorme page will appear on your scree, DO NOT close that browser. Programme check Total2 Parameter also. If unusual sales are observed. It won't wait to decrease %1,5 of coin value, it will sell all coins immediately then it will wait for 2 hours.

### Note : 
This programme just can do buy and sell oparations. You don't need worry about anything.

# Authors
- Umut Can - [linkedin](https://www.linkedin.com/in/umut-can-0a7417157/)
