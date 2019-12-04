# To scrape odds from SportsBet

# I have started by following this tutorial: https://www.edureka.co/blog/web-scraping-with-python/

import re # it's regex
from selenium import webdriver  # selenium is for accessing webpages
import bs4  # BeautifulSoup is for data from websites
import pandas  # pandas is for data analysis

driver = webdriver.Chrome("C:/Users/Liam/PycharmProjects/ArbitrageBetting/drivers/chromedriver.exe")
teamA = []; teamB = []; oddsA = []; oddsB = []  # Arrays for data

url = input("input Sportsbet url: ")
driver.get(url)
content = driver.page_source
soup = bs4.BeautifulSoup(content, features="html.parser")  # soup now contains the html behind url


def fillArrays():
    for i in soup.select('ul > div > ul > li'):  # the tags containing the data for each game are in this structure
        i = str(i)

        # find teamA
        teamAStartIndex = i.find("event-participant-1") + 21
        # 21 because "event-participant-1" is 19 characters, and then there's a " and a >
        teamAEndIndex = i[teamAStartIndex:].find("</span") + teamAStartIndex
        teamA.append(i[teamAStartIndex:teamAEndIndex])

        # find oddsA
        # the odds are after ' "price-text">
        # and are always three digits long (x.xx so four characters)
        oddsAStartIndex = i[teamAStartIndex:].find(
            "price-text") + teamAStartIndex + 12  # "price-text" is 10 chars, plus the ">
        oddsA.append(i[oddsAStartIndex:oddsAStartIndex + 4])

        # find teamB
        teamBStartIndex = i.find("event-participant-2") + 21
        teamBEndIndex = i[teamBStartIndex:].find("</span") + teamBStartIndex
        teamB.append(i[teamBStartIndex:teamBEndIndex])

        # find oddsB
        oddsBStartIndex = i[oddsAStartIndex:].find("price-text") + oddsAStartIndex + 12
        oddsB.append(i[oddsBStartIndex: oddsBStartIndex + 4])


def convertOddsArrayToFloats(array):
    for i in array:
        try:
            i = float(i)
        except ValueError:
            i = 0.00
            print("Betting has been suspended for one game")
        # If betting has been suspended then weird shit shows up where the odds usually are