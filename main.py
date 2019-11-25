# Program for finding arbitrage opportunities
# By Liam Wood-Baker, 2019


# Functions:


def impliedOdds(odds):
    return 1 / odds


# the combined market margin is the sum of the two implied probabilites.
# if it's < 1, then there is an arbitrage opportunity
def combinedMarketMargin(odds1, odds2):
    return (1 / odds1) + (1 / odds2)


# to calculate, given two sets of odds, the two possible comined market margins
def calcMM(odds1, odds2):
    # odds are arrays with two int elements
    MM1 = combinedMarketMargin(odds1[0], odds2[1])
    MM2 = combinedMarketMargin(odds1[1], odds2[0])
    output = [MM1, MM2]
    return sorted(output)


# to keep everything organised, game objects will contain their odds

class Game:

    def __init__(self, name, odds1, odds2):
        self.name = name
        # odds are still two element arrays
        self.odds1 = odds1
        self.odds2 = odds2
        # calculates the best arbitrage opportunity when an object is instantiated
        self.bestArbitrage = calcMM(odds1, odds2)[1]


# to take inputs in the form
# [[A vs B, [odds1a, odds1b], [odds2a, odds2b]],
#  [C vs D, [odds1c, odds1d], [odds2c, odds2d]],
# .
# .
# .
# .
# ]
# and return the best arbs, we can find the lowest CMM for each element, and then return a
# sorted list from low to high

def crunch(array):
    #    array is an array for which each element is an array with 3 elements:
    #    [name, odds1, odds2], where odds are arrays.
    objectArray = []
    for i in array:
        objectArray.append(Game(array[i], array[i], array[i]))

    objectArray.sort(key=lambda game: game.bestArbitrage, reverse=True)
    return objectArray

