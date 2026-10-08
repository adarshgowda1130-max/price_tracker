import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from fake_useragent import UserAgent
import random
import smtplib
load_dotenv()
ua=UserAgent()
amazon_url="https://appbrewery.github.io/instant_pot/"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent":ua.random,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}
data=requests.get(url=amazon_url,headers=headers).text
soup=BeautifulSoup(data,"html.parser")
# print(soup.prettify())
#product price
price=soup.find(class_="a-offscreen").get_text()
actual_price=float(price.split("$")[1])
#product title
product_title=soup.find(id="productTitle").get_text().split("9-in-1")[1]
# print(product_title)
# print(actual_price)
message=f"your product\n{product_title}\n it price is now affordable,it is {actual_price}"

email_name=os.getenv("my_email")
password=os.getenv("email_password")
receiver=os.getenv("to_address")
#     email sender part
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()#this secures our website from 3rd party intercepts

connection.login(user=email_name,password=password)
connection.sendmail(
    from_addr=email_name,
    to_addrs=receiver,
    msg=f"Subject: Price Alert!\n\n{message}".encode('utf-8')
)
connection.close()

