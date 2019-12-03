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
for i in soup.select('ul > div > ul > li'): # the tags containing the data for each game are in this structure
    i = str(i)

    # find teamA
    teamAStartIndex = i.find("event-participant-1") + 21 # 21 because "event-participant-1" is 19 characters, and then there's a " and a >
    teamAEndIndex = i[teamAStartIndex:].find(r"<span") + teamAStartIndex -1
    teamA.append(i[teamAStartIndex:teamAEndIndex])

    # find teamB

    # find oddsA

    # find oddsB

