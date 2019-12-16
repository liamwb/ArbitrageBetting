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
    teamAIndicies = []
    teamBIndicies = []
    oddsAInidicies = []
    oddsBIndicies = []

    soup.find_all()

