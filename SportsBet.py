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
# for i in re.findall("li", soup.body.prettify()):#soup.find_all("li") is a list of all the <li> tags in the soup

