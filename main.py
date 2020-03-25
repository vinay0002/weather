import pandas as pd
import requests
from bs4 import BeautifulSoup
page= requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XnOrCIgzZPZ")
soup=BeautifulSoup(page.content,"html.parser")
seven_day=soup.find(id="seven-day-forecast")
item=seven_day.find_all(class_="tombstone-container")
today=item[0]
period_name=today.find(class_="period-name").get_text()
short_desc=today.find(class_="short-desc").get_text()
temp=today.find(class_="temp").get_text()
# print(period_name)
# print(short_desc)
# print(temp)

period_name=[item.find(class_="period-name").get_text() for item in item]
short_desc=[item.find(class_="short-desc").get_text() for item in item]
temp=[item.find(class_="temp").get_text() for item in item]
print(period_name)
print(short_desc)
print(temp)
wether_stuff = pd.DataFrame (
    {
        'period_name':period_name,
        'short_desc':short_desc,
        'temp':temp
    }
)
print(wether_stuff)
# wether_stuff.to_csv("wether.csv")