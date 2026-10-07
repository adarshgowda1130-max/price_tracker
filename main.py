import requests
from bs4 import BeautifulSoup
amazon_url="https://appbrewery.github.io/instant_pot/"
data=requests.get(url=amazon_url).text
soup=BeautifulSoup(data,"html.parser")
# print(soup.prettify())
price=soup.find(class_="a-offscreen").get_text()
actual_price=float(price.split("$")[1])
print(actual_price)
print(type(actual_price))