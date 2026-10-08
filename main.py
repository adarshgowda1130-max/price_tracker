import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from fake_useragent import UserAgent
import random
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
price=soup.find(class_="a-offscreen").get_text()
# product_title=soup.find(id="productTitle").get_text().split("9-in-1","\t")[1]
# print(product_title)
title = soup.find(id="productTitle").get_text().strip()
print(title)

actual_price=float(price.split("$")[1])
print(actual_price)
# print(type(actual_price))
# load_dotenv()
# api_key=os.getenv("API_KEY")
# print(api_key)