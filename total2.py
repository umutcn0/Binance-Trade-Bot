from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime, timedelta
#09.06.2021 23:32 Güncelleme


total2 = [] #TOTAL2 listesi oluşturuldu.
driver = webdriver.Chrome()
url = "https://tr.tradingview.com/chart/?symbol=CRYPTOCAP%3ATOTAL2"
driver.get(url)
time.sleep(5)
say = 0
b_say = 0  # başlangıç için sayım değişkeni
print("TOTAL2 is ACTİVE")
while True:
    if len(total2) == 2:
        total2stop = float(total2[0]) * 0.985  # %1.5 stop seviyesi

        htmlSource = driver.page_source  # Kaynak kodu elde edildi
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








