# To scrape odds from SportsBet for tennis

# I have started by following this tutorial: https://www.edureka.co/blog/web-scraping-with-python/

import bs4  # BeautifulSoup is for data from websites
from selenium import webdriver  # selenium is for accessing webpages


def getSoup(driver):
    url = "https://www.sportsbet.com.au/betting/sports-home/tennis"
    driver.get(url)
    content = driver.page_source
    soup = bs4.BeautifulSoup(content, features="html.parser")  # soup now contains the html behind url
    return soup



def fillArrays(soup):
    teamA = []
    teamB = []
    oddsA = []
    oddsB = []  # Arrays for data

    for i in soup.select('ul > div > ul > li'):  # the tags containing the data for each game are in this structure
        i = str(i)

        # find teamA
        teamAStartIndex = i.find("event-participant-1") + 21
        # 21 because "event-participant-1" is 19 characters, and then there's a " and a >
        teamAEndIndex = i[teamAStartIndex:].find("<span") + teamAStartIndex
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

    return oddsA, oddsB, teamA, teamB


def convertOddsArrayToFloats(array):
    tempArray = []
    for i in range(0, len(array)):
        try:
            tempArray.append(float(array[i]))
        except ValueError:
            tempArray.append(-1)
            # a negative number will indicate that the odds are in some way out of order,
            # and will be easy to eliminate later
    return tempArray

