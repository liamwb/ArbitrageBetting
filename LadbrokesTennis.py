# To scrape odds from ladbrokes for tennis

import bs4


def getSoup(driver):
    url = "https://www.ladbrokes.com.au/sports/tennis"
    driver.get(url)
    content = driver.page_source
    soup = bs4.BeautifulSoup(content, features="html.parser")  # soup now contains the html behind url
    return soup


def fillArrays(soup):
    teamA = []
    teamB = []
    oddsA = []
    oddsB = []  # Arrays for data

    arrayForNames = soup.find_all(class_="price-button-name")

    for i in range(0, len(arrayForNames)):
        # all the names are stored under this class, so teamA and teamB will alternate
        # names are formatted as follows:
        # <div class="price-button-name">
        #      G. Garcia-Perez/S. Sorribes Tormo
        # </div>
        # so by taking the slice from character 38, then splitting around "<",
        # and then stripping the result, we end up with just the name
        # ie str(i)[38:].split("<")[0].strip()

        if i % 2 == 0:
            teamA.append(str(arrayForNames[i])[38:].split("<")[0].strip())
        elif i % 2 == 1:
            teamB.append(str(arrayForNames[i])[38:].split("<")[0].strip())


    arrayForOdds = soup.find_all(class_="price-button-odds-price")

    # same deal with the odds
    for i in range(0, len(arrayForOdds)):
        # Formatting for the odds is as follows:
        # <div class="price-button-odds-price"><span has-boost="true">2.00</span> <!-- --></div>
        # so using .split(">") gets us a list where the 2nd index has
        # 'x.xx</span'. We just need the first four characters.
        if i % 2 == 0:
            oddsA.append(float(str(arrayForOdds[i]).split(">")[2][0:4]))
        elif i % 2 == 1:
            oddsB.append(float(str(arrayForOdds[i]).split(">")[2][0:4]))
    return oddsA, oddsB, teamA, teamB




