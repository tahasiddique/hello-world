#amazon web scraper by Taha


import requests
import time
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/Apple-MacBook-Pro-9th-Generation-Intel-Core-i9/dp/B07SDPJ531/ref=sr_1_10?keywords=macbook+pro&qid=1568561733&sr=8-10"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").getText()
    price = soup.find(id="priceblock_ourprice").getText()

    converted_price = price[1:10].replace(',', ',')
    converted_price = ''.join([ch for ch in converted_price if ch in '0123456789.'])
    converted_price = float(converted_price)

    # print(price)

    if (converted_price < 220000):
        send_mail()
        time.sleep(3)
        print(title.strip())
        print(converted_price)
    else:
        print(title.strip())
        print("Price is still",converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('siddiquit541@gmail.com', 'kucgwkprwkdqbzyj')

    subject = 'price fell down'
    body = 'Check the amazon link https://www.amazon.in/Apple-MacBook-Pro-9th-Generation-Intel-Core-i9/dp/B07SDPJ531/ref=sr_1_10?keywords=macbook+pro&qid=1568561733&sr=8-10 ' \


    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'siddiquit541gmail.com',
        'antsinfinites@gmail.com',
        msg
    )
    print("Email Has Been Sent")

    server.quit()
check_price()
