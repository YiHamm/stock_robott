import requests
import time
from bs4 import BeautifulSoup

stock = ['1101','2330','5347']

for i in range(len(stock)):
  stockid = stock[i]
  url = 'https://tw.stock.yahoo.com/quote/'+stockid+'.TW'
  r = requests.get(url)
  soup = BeautifulSoup(r.text,'html.parser')
  price = soup.find('span',class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)"])
  if price == None :
    url = 'https://tw.stock.yahoo.com/quote/'+stockid+'.TWO'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    price = soup.find('span',class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)"])
  price = price.getText()
  #bot
  message = '股票' + stockid + '的即時價格為: ' + price
  #bot token(telegram_botfather)
  token = '6949107486:AAFStrChPqLmYXyDQ7bHCGa-LJD_gGgivBI'
  #chat_id(user)
  chat_id = '6837535478'
  #send message
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
  requests.get(url)
  #停3秒
  time.sleep(3)  
