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

