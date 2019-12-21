# To scrape data from Neds for tennis

import bs4  # BeautifulSoup is for data from websites
from selenium import webdriver  # selenium is for accessing webpages
import main

driver = webdriver.Chrome("C:/Users/Liam/PycharmProjects/ArbitrageBetting/drivers/chromedriver.exe")
teamA = []; teamB = []; oddsA = []; oddsB = []  # Arrays for data

url = input("input Neds url: ")
driver.get(url)
content = driver.page_source
soup = bs4.BeautifulSoup(content, features="html.parser")  # soup now contains the html behind url

def fillArrays():
    pbnArray = soup.find_all(class_="price-button-name")
    # every even index is the name of a teamA, and vice-versa for the odd indicies
    for i in range(0, len(pbnArray)):
        if i % 2 == 0:
            teamA.append(i)
        elif i % 2 == 1:
            teamB.append(i)

fillArrays()
