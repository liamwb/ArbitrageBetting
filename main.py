# Program for finding arbitrage opportunities
# By Liam Wood-Baker, 2019


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
# to the same real life game. Team A will come first alphabetically

class Game:
    def __init__(self, bettingAgency, teamA, teamB, oddsA, oddsB, ):
        self.bettingAgency = bettingAgency
        self.teamA = teamA
        self.teamB = teamB
        self.oddsA = oddsA
        self.oddsB = oddsB
        self.impliedOddsA = 1 / oddsA
        self.impliedOddsB = 1 / oddsB

# now a function to find the lowest combinedMM for several sets of odds on the same game
# (but different Game objects!)

def findLeastCMM(*games):
    for i in games:
        print(i.bettingAgency)
    return


