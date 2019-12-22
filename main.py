# Program for finding arbitrage opportunities
# By Liam Wood-Baker, 2019


import NedsTennis
import SportsBetTennis
import bs4  # BeautifulSoup is for data from websites
from selenium import webdriver  # selenium is for accessing webpages

# Variables
myDriver = webdriver.Chrome("C:/Users/Liam/PycharmProjects/ArbitrageBetting/drivers/chromedriver.exe")
allGameObjects = []


# Classes:

class Game:
    def __init__(self, bettingAgency, teamA, teamB, oddsA, oddsB, ):
        self.bettingAgency = bettingAgency
        self.teamA = teamA
        self.teamB = teamB
        self.oddsA = oddsA
        self.oddsB = oddsB
        self.impliedOddsA = 1 / oddsA
        self.impliedOddsB = 1 / oddsB

        # to find different odds on the same game, each Game object will have a gameID made up of the
        # last word of teamA + the last word of teamB, all in lowercase, with no spaces or punctuation.
        # It seems unlikely that this will ever be non-unique.

        idpartA = teamA.replace(".", " ").replace("-", " ").replace("/", " ").split()[-1].lower().strip()
        idpartB = teamB.replace(".", " ").replace("-", " ").replace("/", " ").split()[-1].lower().strip()
        self.gameID = idpartA + idpartB


class PossibleArbitrage:
    def __init__(self, teamA, teamB, oddsA, oddsB, agencyA, agencyB):
        self.teamA = teamA
        self.teamB = teamB
        self.oddsA = oddsA
        self.oddsB = oddsB
        self.agencyA = agencyA
        self.agencyB = agencyB
        self.CMM = combinedMarketMargin(oddsA, oddsB)


# Functions:

def impliedOdds(odds):
    return 1 / odds


# the combined market margin is the sum of the two implied probabilites.
# if it's < 1, then there is an arbitrage opportunity
def combinedMarketMargin(odds1, odds2):
    return (1 / odds1) + (1 / odds2)


# If there is an arbitrage opportunity, then to calculate the profit for a
# given investment the following formula is used:
#
# Profit = (Investment / combined market margin) – Investment
def profit(investment, combinedMarketMargin):
    return (investment / combinedMarketMargin) - investment


# To calculate how much to stake on each side of the arbitrage bet, the following formula is used:
#
# Individual bets = (Investment x Individual implied odds) / combined market margin
def individualBet(investment, individualImpliedOdds, combinedMarketMargin):
    return (investment * individualImpliedOdds) / combinedMarketMargin


# Given several odds on a single game, we want to find the lowest CombinedMM available.
# Let's try and approach this in an Object Oriented way, by creating an object for each set of
# odds, for each game. Teams A and B must refer to the same teams across all Game objects that refer
# to the same real life game.


def createGameObjects(oddsA, oddsB, teamA, teamB, bettingAgency):
    gameObjects = []
    for i in range(0, len(teamA)):
        gameObjects.append(
            Game(bettingAgency, teamA[i], teamB[i], oddsA[i], oddsB[i])
        )
    return gameObjects


# now a function to find the lowest combinedMM for several sets of odds on the same game
# (but different Game objects!)


# the url for SportsbetTennis is https://www.sportsbet.com.au/betting/sports-home/tennis

def scrapeSportsBetTennis():
    soup = SportsBetTennis.getSoup(myDriver)
    oddsA, oddsB, teamA, teamB = SportsBetTennis.fillArrays(soup)
    oddsA = SportsBetTennis.convertOddsArrayToFloats(oddsA)
    oddsB = SportsBetTennis.convertOddsArrayToFloats(oddsB)
    gameObjects = createGameObjects(oddsA, oddsB, teamA, teamB, "sportsbet")
    return gameObjects


# the url for NedsTennisis https://www.neds.com.au/sports/tennis

def scrapeNedsTennis():
    soup = NedsTennis.getSoup(myDriver)
    oddsA, oddsB, teamA, teamB = NedsTennis.fillArrays(soup)
    gameObjects = createGameObjects(oddsA, oddsB, teamA, teamB, "neds")
    return gameObjects


allGameObjects.extend(scrapeNedsTennis())
allGameObjects.extend(scrapeSportsBetTennis())

for i in allGameObjects:
    print(i.teamA + " vs " + i.teamB + " at " + str(i.oddsA) + " vs " + str(i.oddsB) + " through " + i.bettingAgency)


def findGamesInCommon(gameObjects):
    dict = {}
    for i in gameObjects:
        # check if a game with the same gameID has already been added to dict
        matchFound = False
        currentGameID = i.gameID
        # j is a gameID (one of the ones already added to dict, i is a Game object
        for j in dict:
            if currentGameID == j:
                matchFound = True
                break

        if matchFound:
            dict[currentGameID].append(i)
        if not matchFound:
            dict[currentGameID] = [i]

    output = {}
    for i in dict:
        if len(dict[i]) > 1:  # ie if there's more than one set of odds on a game
            output[i] = dict[i]
    # now dict contains only those games with more than one set of odds on them

    return output


allCommonGames = findGamesInCommon(allGameObjects)


# Now, given allCommonGames, we need to find the lowest CMM

def arrangeByCMM(gamesInCommon):
    possibleArbitrages = []

    # Because gamesInCommon is a dictionary
    for games in gamesInCommon:
        gamesList = gamesInCommon[games]

        for game1 in gamesList:
            for game2 in gamesList:
                possibleArbitrages.append(PossibleArbitrage(
                    game1.teamA, game2.teamB,
                    game1.oddsA, game2.oddsB,
                    game1.bettingAgency, game2.bettingAgency))

    # we now have an unsorted list of all the various permutations of all the games
    # which have several sets of odds given for them. We now need to sort this list
    # so that the game with the lowest CMM is at the top of the list

    possibleArbitrages.sort(key=lambda x: x.CMM)

    # For future reference this is the first time I've ever used a lambda

    return possibleArbitrages