import numpy as np
import pandas as pd
import talib as talib
import talib.abstract as tb
from binance.client import Client
from datetime import datetime, timedelta
import requests
import telebot
import traceback
import sys
from os import path
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from threading import *
#09.06.2021 22:20 Updated

Bot_Token = "" # Telegram Bot Token
Chat_ID = "" # Telegram group chat id
TradeBot = telebot.TeleBot(Bot_Token)


class Bot():
    coins = ['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'GASBTC', 'WTCBTC', 'LRCBTC', 'DODOBTC', 'FRONTBTC',
             'QTUMBTC', 'OMGBTC', 'ZRXBTC', 'BQXBTC', 'KNCBTC', 'IOTABTC', 'LINKBTC', 'MDABTC', 'MTLBTC',
             'EOSBTC', 'TFUELBTC', 'CAKEBTC', 'ETCBTC', 'ZECBTC', 'BNTBTC', 'ASTBTC', 'DASHBTC', 'LSKBTC',
             'XRPBTC', 'ARKBTC', 'ENJBTC', 'ZILBTC', 'ONTBTC', 'DCRBTC', 'PHABTC', 'TVKBTC', 'STORJBTC',
             'KMDBTC', 'RCNBTC', 'NULSBTC', 'XMRBTC', 'BATBTC', 'GXSBTC', 'ALICEBTC', 'LINABTC', 'PERPBTC',
             'MANABTC', 'ADXBTC', 'ADABTC', 'PPTBTC', 'XLMBTC', 'WAVESBTC', 'ICXBTC', 'ELFBTC', 'AIONBTC',
             'NAVBTC', 'VIABTC', 'BLZBTC', 'SNXBTC', 'IRISBTC', 'UNFIBTC', 'RLCBTC', 'PIVXBTC', 'STEEMBTC',
             'NEARBTC', 'FILBTC', 'NANOBTC', 'XEMBTC', 'WANBTC', 'SYSBTC', 'GRSBTC', 'SUSHIBTC', 'EASYBTC',
             'REPBTC', 'SKYBTC', 'CVCBTC', 'THETABTC', 'AGIBTC', 'DATABTC', 'ARDRBTC', 'POLYBTC', 'RVNBTC',
             'RENBTC', 'ONGBTC', 'FETBTC', 'MATICBTC', 'CRVBTC', 'SANDBTC', 'ATOMBTC', 'ONEBTC', 'FTMBTC',
             'ALGOBTC', 'DUSKBTC', 'PONDBTC', 'DEGOBTC', 'TOMOBTC', 'PERLBTC', 'CHZBTC', 'BANDBTC', 'XTZBTC',
             'HBARBTC', 'NKNBTC', 'STXBTC', 'KAVABTC', 'BCHBTC', 'VITEBTC', 'FTTBTC', 'OGNBTC', 'LTOBTC',
             'COTIBTC', 'SOLBTC', 'CTSIBTC', 'HIVEBTC', 'CHRBTC', 'PNTBTC', 'COMPBTC', 'SXPBTC', 'MKRBTC',
             'RUNEBTC', 'FIOBTC', 'YFIBTC', 'SRMBTC', 'ANTBTC', 'OCEANBTC', 'DOTBTC', 'LUNABTC', 'IDEXBTC',
             'RSRBTC', 'TRBBTC', 'BZRXBTC', 'KSMBTC', 'EGLDBTC', 'DIABTC', 'WINGBTC', 'UNIBTC', 'OXTBTC',
             'AVAXBTC', 'HNTBTC', 'FLMBTC', 'SCRTBTC', 'ORNBTC', 'UTKBTC', 'XVSBTC', 'ALPHABTC', 'VIDTBTC',
             'AAVEBTC', 'INJBTC', 'AERGOBTC', 'AUDIOBTC', 'CTKBTC', 'AXSBTC', 'HARDBTC', 'STRAXBTC', 'ROSEBTC',
             'SKLBTC', 'GLMBTC', 'GRTBTC', 'PSGBTC', '1INCHBTC', 'SFPBTC']

    min_amount_dict = {'ETHBTC': '3', 'LTCBTC': '2', 'BNBBTC': '2', 'NEOBTC': '0', 'GASBTC': '2', 'WTCBTC': '2',
                       'LRCBTC': '0', 'DODOBTC': '1', 'FRONTBTC': '1', 'QTUMBTC': '2', 'OMGBTC': '2', 'ZRXBTC': '0',
                       'BQXBTC': '0', 'KNCBTC': '0', 'IOTABTC': '0', 'LINKBTC': '1', 'MDABTC': '0', 'MTLBTC': '0',
                       'EOSBTC': '2', 'TFUELBTC': '0', 'CAKEBTC': '2', 'ETCBTC': '2', 'ZECBTC': '3', 'BNTBTC': '1',
                       'ASTBTC': '0', 'DASHBTC': '3', 'LSKBTC': '2', 'XRPBTC': '0', 'ARKBTC': '0', 'ENJBTC': '0',
                       'ZILBTC': '0', 'ONTBTC': '2', 'DCRBTC': '3', 'PHABTC': '0', 'TVKBTC': '0', 'STORJBTC': '0',
                       'KMDBTC': '2', 'RCNBTC': '0', 'NULSBTC': '0', 'XMRBTC': '3', 'BATBTC': '0', 'GXSBTC': '0',
                       'ALICEBTC': '1', 'LINABTC': '0', 'MANABTC': '0', 'ADXBTC': '0', 'ADABTC': '0', 'PPTBTC': '0',
                       'XLMBTC': '0', 'WAVESBTC': '2', 'ICXBTC': '0', 'ELFBTC': '0', 'AIONBTC': '0', 'NAVBTC': '0',
                       'VIABTC': '0', 'BLZBTC': '0', 'SNXBTC': '2', 'IRISBTC': '0', 'UNFIBTC': '1', 'RLCBTC': '0',
                       'PIVXBTC': '0', 'STEEMBTC': '0', 'NEARBTC': '2', 'FILBTC': '2', 'NANOBTC': '0', 'XEMBTC': '0',
                       'WANBTC': '0', 'SYSBTC': '0', 'GRSBTC': '0', 'SUSHIBTC': '2', 'EASYBTC': '2', 'REPBTC': '3',
                       'SKYBTC': '0', 'CVCBTC': '0', 'THETABTC': '1', 'AGIBTC': '0', 'DATABTC': '0', 'ARDRBTC': '0',
                       'POLYBTC': '0', 'PERPBTC': '2', 'RVNBTC': '0', 'RENBTC': '0', 'ONGBTC': '0', 'FETBTC': '0',
                       'MATICBTC': '0', 'CRVBTC': '2', 'SANDBTC': '0', 'ATOMBTC': '2', 'ONEBTC': '0', 'FTMBTC': '0',
                       'ALGOBTC': '0', 'DUSKBTC': '0', 'PONDBTC': '0', 'DEGOBTC': '2', 'TOMOBTC': '0', 'PERLBTC': '0',
                       'CHZBTC': '0', 'BANDBTC': '1', 'XTZBTC': '2', 'HBARBTC': '0', 'NKNBTC': '0', 'STXBTC': '0',
                       'KAVABTC': '1', 'BCHBTC': '3', 'VITEBTC': '0', 'FTTBTC': '2', 'OGNBTC': '0', 'LTOBTC': '0',
                       'COTIBTC': '0', 'SOLBTC': '1', 'CTSIBTC': '0', 'HIVEBTC': '0', 'CHRBTC': '0', 'PNTBTC': '0',
                       'COMPBTC': '3', 'SXPBTC': '0', 'MKRBTC': '3', 'RUNEBTC': '1', 'FIOBTC': '0', 'YFIBTC': '4',
                       'SRMBTC': '0', 'ANTBTC': '2', 'OCEANBTC': '0', 'DOTBTC': '1', 'LUNABTC': '0', 'IDEXBTC': '0',
                       'RSRBTC': '0', 'TRBBTC': '3', 'BZRXBTC': '0', 'KSMBTC': '3', 'EGLDBTC': '3', 'DIABTC': '2',
                       'WINGBTC': '3', 'UNIBTC': '1', 'OXTBTC': '0', 'AVAXBTC': '1', 'HNTBTC': '2', 'FLMBTC': '0',
                       'SCRTBTC': '0', 'ORNBTC': '2', 'UTKBTC': '0', 'XVSBTC': '2', 'ALPHABTC': '0', 'VIDTBTC': '0',
                       'AAVEBTC': '2', 'INJBTC': '1', 'AERGOBTC': '0', 'AUDIOBTC': '0', 'CTKBTC': '1', 'AXSBTC': '0',
                       'HARDBTC': '1', 'STRAXBTC': '1', 'ROSEBTC': '0', 'SKLBTC': '0', 'GLMBTC': '0', 'GRTBTC': '0',
                       'PSGBTC': '2', '1INCHBTC': '1', 'TWTBTC': '0', 'SFPBTC': '0'}

    interval = '15m'
    signal_position = list()  # list of coins with buy signals
    stop_coin = list()  # list of stopped coins
    stop_dict = dict()
    indicator = pd.DataFrame()
    coin_excel = pd.DataFrame(
        columns=["Coin", "BuyTime", "Position1", "BuyPrice", "BinanceBuy"])  # the table where the purchased coins are written
    trade_excel = pd.DataFrame(columns=["Coin", "SellTime", "Position2", "SellPrice", "Binance Price", "Kar-zarar",
                                        "Binance-marj", "Status"])  # the table where the sold coins are written
    allcoin_trade = pd.DataFrame(
        columns=["BuyTime", "Coin", "Position1", "BuyPrice", "SellTime", "Position2", "SellPrice", "Kar-zarar"])
    latestBalanceTime = None

    global price, buytime, binance_marj, binance_price, vwmacd_cross_up, vwmacd, signal, hist, sell_all_coins_signal, total2_durum
    global high, low, close, old_plus, old_minus, upperBB, lowerBB, old_upperBB, old_lowerBB, deger, plus, minus, middleBB, old_middleBB

    def __init__(self):
        self.sell_all_coins_signal = 0
        self.KEY = '' #Binance KEY
        self.SECRET = '' #Binance SECRET
        self.client = Client(self.KEY, self.SECRET)
        self.total2_durum = False  # Initial value for the program to process
        self.sell_all_coins_signal = 0




    def __readPositionsFromFile(self):  # to read open positions
        if path.exists('signal_position.txt'):
            print("signal_position.txt found, reading")
            with open('signal_position.txt', newline='') as file:
                signal_position = [l.strip() for l in file]
                print(signal_position)

    def __writePositionsToFile(self, coin):  # to write open positions
        with open('signal_position.txt', 'w') as filehandle:
            filehandle.writelines("%s\n" % s for s in self.signal_position)

    def run(self):
        print("Bot is running")
        self.PrintBalancesToTelegram()
        while True:
            if len(self.signal_position) < 5:
                for coin in self.coins:
                    self.Coin_search(coin)
                    try:
                        var = 0

                        if len(self.signal_position) > 0 and len(
                                self.signal_position) <= 4:  # IS THE COIN INCLUDED IN THE LIST?
                            for i in self.signal_position:
                                if coin == i:
                                    var = 1

                        if self.total2_durum == False and self.price < self.middleBB and var == 0 and len(
                                self.signal_position) <= 4 and self.vwmacd_cross_up and self.IIP21 > 0:
                            self.Buy(coin)

                        for i in self.signal_position:
                            if coin == i:
                                self.Coin_search(i)
                                self.Sell(i)

                    except Exception:
                        traceback.print_exception(*sys.exc_info())
                        time.sleep(100)
                        self.client = Client(self.KEY, self.SECRET)
                        time.sleep(20)
                        pass


            elif len(self.signal_position) == 5:
                try:
                    for i in self.signal_position:
                        self.Coin_search(i)
                        self.Sell(i)


                except Exception:
                    traceback.print_exception(*sys.exc_info())
                    time.sleep(100)
                    self.client = Client(self.KEY, self.SECRET)
                    time.sleep(20)
                    pass


        self.coin_excel.to_excel('buycoins1.xlsx')
        self.PrintBalancesToTelegram()
        # self.stopWaiting()

    def stopWaiting(self):  # Don't buy the coin for 2 hours if it stopped
        try:
            now = datetime.now()
            for i in self.stop_dict.items():
                if i[1] + timedelta(hours=2) <= now:
                    stop_name = i[0]
                    self.stop_coin.remove(stop_name)
                    self.coins.append(stop_name)
        except:
            pass

    def Buy(self, coin):
        min_amount = int(Bot.min_amount_dict[coin])
        amount = self.amount_btc() / float(self.price)
        amount = round(amount, min_amount)

        self.client.create_order(symbol=coin, side="BUY", type="MARKET", quantity=amount)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        buytime = dt_string + " " + coin
        self.binanceBuy = self.client.get_my_trades(symbol=coin, limit=1)
        self.binanceBuy = float(self.binanceBuy[0]['price'])
        message = "**** BUY **** \nCoin: {} \nAmount: {}\nTime: {} \nPRICE : {}\nBinanceBuy: {}".format(coin, amount,
                                                                                                        dt_string,
                                                                                                        "%.8f" % self.price,
                                                                                                        "%.8f" % self.binanceBuy)
        print(message)
        self.coin_excel = self.coin_excel.append(
            {'BuyTime': buytime, 'Coin': coin, 'Position1': "BUY", 'BuyPrice': "%.8f" % self.price,
             "BinanceBuy": "%.8f" % self.binanceBuy},
            ignore_index=True)
        self.signal_position.append(coin)
        self.__writePositionsToFile(coin)
        self.SendToTelegram(message)
        self.btc_balance()

    def Sell(self, coin):

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        coin_buyprice = self.coin_excel[self.coin_excel["Coin"] == coin]["BuyPrice"].head(1)
        self.binance_buyprice = self.coin_excel[self.coin_excel["Coin"] == coin]["BinanceBuy"].head(1)
        stop_price = float(self.binance_buyprice) * 0.97
        self.deger = (((float(self.price) / float(coin_buyprice)) * 100) - 100)

        if self.sell_all_coins_signal == 1:
            self.Coin_search(coin)
            self.deger = (((float(self.price) / float(coin_buyprice)) * 100) - 100)
            self.Sold(coin, self.price, self.deger)

        elif self.total2_durum == True:
            self.sell_all_coins()

        elif self.price >= self.upperBB:
            self.Sold(coin, self.price, self.deger)
            message = "**** SELL **** \nCoin: {}\nTime: {} \nPRİCE : {}\nBinance Price :{}\nMarj:%{}\nBinance Marj:%{}".format(
                coin, dt_string,
                "%.8f" % self.price, "%.8f" % self.binance_price,
                "%.2f" % self.deger, "%.2f" % self.binance_marj)
            self.SendToTelegram(message)
            print(message)

        elif self.price <= stop_price:
            self.Sold(coin, self.price, self.deger)
            message = "**** STOP **** \nCoin: {}\nTime: {} \nPRİCE : {}\nBinance Price :{}\nMarj:%{}\nBinance Marj:%{}".format(
                coin, dt_string,
                "%.8f" % self.price, "%.8f" % self.binance_price,
                "%.2f" % self.deger, "%.2f" % self.binance_marj)
            self.SendToTelegram(message)

            """if self.allcoin_trade.shape[0] > 3:
                last1 = self.allcoin_trade["Status"].iloc[-1]
                last2 = self.allcoin_trade["Status"].iloc[-2]
                if last1 == "Loss" and last2 == "Loss":
                    self.sell_all_coins()

            elif last1 == "Waited" and last2 == "Waited":
                message = "2 WAİTED + 1 STOP COİN\n WAİTİNG 1 MORE HOUR"""

            """self.stop_coin.append(coin)  # stop coin listesine ekledi
            self.coins.remove(coin)  # coini listeden sil
            self.stop_dict.update({coin: now})"""

            # if self.allcoin_trade["Kar-zarar"].iloc[:-1][0] < 0 and self.allcoin_trade["Kar-zarar"].iloc[:-2][0] < 0:

            print(message)

    def sell_all_coins(self):
        message = "TOTAL2 ALERT - ALL COİNS ARE SELLİNG"
        self.SendToTelegram(message)
        self.sell_all_coins_signal = 1
        for coin in self.signal_position:
            self.Sell(coin)
        self.sell_all_coins_signal = 0
        while self.total2_durum :
            time.sleep(300)  # 5 dakika beklemeye gir.


        """self.allcoin_trade["Status"].iloc[-1] = "Waited"
        self.allcoin_trade["Status"].iloc[-2] = "Waited"
        message = "DOUBLE STOP WAİT FOR 30 MİNUTES
        self.SendToTelegram(message)"""

    def Coin_search(self, coin):
        self.klines = self.client.get_klines(symbol=coin, interval=self.interval, limit=40)
        self.array = np.array(self.klines, dtype=np.float32)

        self.df = pd.DataFrame(data=self.array[:, 0:6], columns=["date", "open", "high", "low", "close", "volume"])

        self.price = self.df["close"][len(self.df) - 1]
        self.high = [float(entry[2]) for entry in self.klines]
        self.low = [float(entry[3]) for entry in self.klines]
        self.close = [float(entry[4]) for entry in self.klines]
        self.volume = [float(entry[5]) for entry in self.klines]

        self.close_array = np.asarray(self.close)
        self.high_array = np.asarray(self.high)
        self.low_array = np.asarray(self.low)
        self.volume_array = np.asarray(self.volume)
        self.close_finished = self.close_array[:-1]
        self.plus_di = tb.PLUS_DI(self.df, timeperiod=20)
        self.minus_di = tb.MINUS_DI(self.df, timeperiod=20)
        self.upperBB, self.lowerBB, self.old_upperBB, self.old_lowerBB, self.middleBB, self.old_middleBB = self.BBANDS(
            self.df, length=20, mult=1.75)

        # self.vwmacd, self.signal, self.hist = self.VWMACD(df=self.df)
        # self.vwmacd_cross_up= self.vwmacd[-2]<self.signal[-2] and self.vwmacd[-1]>self.signal[-1]
        fastperiod = 12
        slowperiod = 26
        signalperiod = 9
        self.indicator["fastMA"] = talib.EMA(self.df["volume"] * self.df["close"], fastperiod) / talib.EMA(
            self.df["volume"], fastperiod)
        self.indicator["slowMA"] = talib.EMA(self.df["volume"] * self.df["close"], slowperiod) / talib.EMA(
            self.df["volume"], slowperiod)
        self.indicator["vwmacd"] = self.indicator["fastMA"] - self.indicator["slowMA"]
        self.indicator["signal"] = talib.EMA(self.indicator["vwmacd"], signalperiod)
        self.indicator["hist"] = self.indicator["vwmacd"] - self.indicator["signal"]
        self.vwmacd = self.indicator["vwmacd"][len(self.indicator["vwmacd"]) - 1]
        self.old_vwmacd = self.indicator["vwmacd"][len(self.indicator["vwmacd"]) - 2]
        self.signal = self.indicator["signal"][len(self.indicator["signal"]) - 1]
        self.old_signal = self.indicator["signal"][len(self.indicator["signal"]) - 2]
        self.old2_vwmacd = self.indicator["vwmacd"][len(self.indicator["vwmacd"]) - 3]
        self.old2_signal = self.indicator["signal"][len(self.indicator["signal"]) - 3]
        self.vwmacd_cross_up = self.old2_vwmacd < self.old2_signal and self.old_vwmacd > self.old_signal and self.vwmacd > self.signal
        self.indicator['II'] = (2 * self.df['close'] - self.df['high'] - self.df['low']) / (
                self.df['high'] - self.df['low']) * self.df['volume']
        self.indicator['IIP21'] = (self.indicator['II'].rolling(window=21).sum()) / (
            self.df['volume'].rolling(window=20).sum()) * 100
        self.IIP21 = self.indicator['IIP21'][len(self.indicator['IIP21']) - 1]

    def Sold(self, coin, price, deger):
        self.balance = self.client.get_account()["balances"]
        min_amount = int(Bot.min_amount_dict[coin])
        for x in self.balance:
            if x['asset'] == coin[:-3]:
                amount = float(x['free'])
                amount = round(amount, min_amount)

        self.client.create_order(symbol=coin, side="SELL", type="MARKET", quantity=amount)
        self.btc_balance()

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        self.binance_price = self.client.get_my_trades(symbol=coin, limit=1)
        self.binance_price = float(self.binance_price[0]['price'])
        self.binance_buyprice = self.coin_excel[self.coin_excel["Coin"] == coin]["BinanceBuy"].head(1)
        self.binance_marj = ((float(self.binance_price) / float(self.binance_buyprice) * 100) - 100)

        if float(self.binance_marj) < 0:
            self.trade_excel = self.trade_excel.append(
                {'Coin': coin, 'Position2': "SELL", 'SellPrice': "%.8f" % price,
                 'Kar-zarar': "%.2f" % deger,
                 "SellTime": dt_string, "Binance Price": self.binance_price, "Binance-marj": self.binance_marj,
                 "Status": "Loss"},
                ignore_index=True)
        else:
            self.trade_excel = self.trade_excel.append(
                {'Coin': coin, 'Position2': "SELL", 'SellPrice': "%.8f" % price,
                 'Kar-zarar': "%.2f" % deger,
                 "SellTime": dt_string, "Binance Price": self.binance_price, "Binance-marj": self.binance_marj,
                 "Status": "Profit"},
                ignore_index=True)

        merge_excel = pd.merge(self.coin_excel, self.trade_excel, on=['Coin'])
        self.allcoin_trade = self.allcoin_trade.append(merge_excel, ignore_index=True)
        self.allcoin_trade.to_excel('Trade_hist.xlsx')
        self.signal_position.remove(coin)

        self.__writePositionsToFile(coin)
        print(self.signal_position)
        c_coin = "Current coins:\n {}".format(self.signal_position)
        self.SendToTelegram(c_coin)

        self.trade_excel = self.trade_excel.set_index('Coin')
        self.trade_excel.drop(labels=coin, inplace=True, axis=0)
        self.trade_excel.reset_index(inplace=True)

        self.coin_excel = self.coin_excel.set_index('Coin')
        self.coin_excel.drop(labels=coin, inplace=True, axis=0)
        self.coin_excel.reset_index(inplace=True)

    def amount_btc(self):

        btc_amount = self.btc_balance()

        if len(self.signal_position) == 0:
            amount_btc = btc_amount * 0.20
            return amount_btc
        elif len(self.signal_position) == 1:
            amount_btc = btc_amount * 0.25
            return amount_btc
        elif len(self.signal_position) == 2:
            amount_btc = btc_amount * 0.33
            return amount_btc
        elif len(self.signal_position) == 3:
            amount_btc = btc_amount * 0.5
            return amount_btc
        elif len(self.signal_position) == 4:
            amount_btc = btc_amount * 0.98
            return amount_btc

    def btc_balance(self):
        self.balance = self.client.get_account()["balances"]

        for i in self.balance:
            if i['asset'] == 'BTC':
                btc = float(i['free'])
                return btc

    def BBANDS(self, df, length, mult):
        bbands = tb.BBANDS(df * 100000, nbdevup=mult, nbdevdn=mult, timeperiod=length)
        upperBB = bbands["upperband"] / 100000
        lowerBB = bbands["lowerband"] / 100000
        middleBB = bbands["middleband"] / 100000
        return upperBB[len(upperBB) - 1], lowerBB[len(lowerBB) - 1], upperBB[len(upperBB) - 2], lowerBB[
            len(lowerBB) - 2], middleBB[len(middleBB) - 1], middleBB[len(middleBB) - 2]

    def PrintBalancesToTelegram(self):
        now = datetime.now()
        if self.latestBalanceTime is None or self.latestBalanceTime + timedelta(minutes=60) < now:
            message = "Balances"
            balances = self.client.get_account()["balances"]
            for x in balances:
                # print(x)
                if float(x["free"]) >= 0.5:
                    message = "{}\r\n   Coin: {}, Amount: {}".format(message, x["asset"], x["free"])
            self.SendToTelegram(message)
            self.latestBalanceTime = now

    def SendToTelegram(self, message):
        requests.post(
            "https://api.telegram.org/bot" + Bot_Token + "/sendMessage?chat_id=" + Chat_ID + "&text=" + message)

    def Total2_value_bot(self):
        total2 = []  # TOTAL2 list created.
        driver = webdriver.Chrome()
        url = "https://tr.tradingview.com/chart/?symbol=CRYPTOCAP%3ATOTAL2"
        driver.get(url)
        time.sleep(5)
        say = 0
        b_say=0 # number variable for start
        print("TOTAL2 is ACTİVE")
        while True:
            if len(total2) == 2:
                total2stop = float(total2[0]) * 0.985  # %1.5 stop loss

                htmlSource = driver.page_source  # Source code obtained
                soup = BeautifulSoup(htmlSource, "html.parser")
                doviz_deger = soup.find("span", {"class": "priceWrapper-3PT2D-PK"}).text
                total2_value = doviz_deger[:-4]
                self.total2_durum = float(total2_value) < float(total2stop)  # TRUE FALSE DEĞER DÖNECEK , STOP OLMAYACAKSA FALSE (DEVAM).. STOP OLACAKSA TRUE (DUR)
                time.sleep(10)
                say += 1

                if say == 90:
                    say = 0
                    total2.pop(0)
                    total2.append(total2_value)
                return self.total2_durum

            else:
                while b_say != 180:
                    htmlSource = driver.page_source
                    soup = BeautifulSoup(htmlSource, "html.parser")
                    doviz_deger = soup.find("span", {"class": "priceWrapper-3PT2D-PK"}).text
                    total2_value = doviz_deger[:-4]
                    if b_say == 89 or b_say == 179:
                        total2.append(total2_value)
                    time.sleep(10)
                    b_say += 1

#Parallel Programming for to check Total2. İf Total2 value decrease it will sell all coins immediately

bot = Bot()

t1 = Thread(target=bot.Total2_value_bot)
t2 = Thread(target=bot.run)
t2.start()
t1.start()

t1.join()
t2.join()
















