# To scrape data from Neds for tennis

import bs4  # BeautifulSoup is for data from websites
from selenium import webdriver  # selenium is for accessing webpages


def getSoup(driver):
    url = "https://www.neds.com.au/sports/tennis"
    driver.get(url)
    content = driver.page_source
    soup = bs4.BeautifulSoup(content, features="html.parser")  # soup now contains the html behind url
    return soup


def fillArrays(soup):
    teamA = []
    teamB = []
    oddsA = []
    oddsB = []  # Arrays for data
    pbnArray = soup.find_all(class_="price-button-name")
    # every even index is the name of a teamA, and vice-versa for the odd indicies

    # each bit of text starts with the following:
    # </div>, <div class="price-button-name">
    # which is 38 characters long. So the name will start at the 40th character, and will be followed by a newline
    # this mean we can get the name by calling .split('\n') and then taking the zeroth member of the resulting list.
    # hence the fairly ugly .append(str(pbnArray[i])[38:].split("\n")[0])
    for i in range(0, len(pbnArray)):
        if i % 2 == 0:
            teamA.append(str(pbnArray[i])[38:].split("\n")[0])
        elif i % 2 == 1:
            teamB.append(str(pbnArray[i])[38:].split("\n")[0])

    oddsArray = soup.find_all(class_="price-button-odds-price")
    # As before, every even index will be an OddsA, and every odd an OddsB

    # there is quite a bit of junk preceding the odds each time, but by calling .split(">"),
    # we can get a list with the odds at the beginning of the second index. From there, the
    # odds occupy four characters (x.xx), so we have:
    # str(oddsArray[i])           so I can slice to the bit I want
    #                  .split(">") to skip up to the start of the odds
    #                             [2]     to get to the right bit
    #                                [0:4] for just the x.xx odds

    for i in range(0, len(oddsArray)):
        if i % 2 == 0:
            oddsA.append(float(str(oddsArray[i]).split(">")[2][0:4]))
        elif i % 2 == 1:
            oddsB.append(float(str(oddsArray[i]).split(">")[2][0:4]))

    return oddsA, oddsB, teamA, teamB

