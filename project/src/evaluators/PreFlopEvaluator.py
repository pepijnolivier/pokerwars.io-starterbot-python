import os.path
import csv


class PreFlopEvaluator:

    def getRanking(self, cards, rankingMap):

        cardOneVal = cards[0].getValue()
        cardTwoVal = cards[1].getValue()

        representation = str(cardOneVal + '-' + cardTwoVal)
        return rankingMap[representation]

    def evaluatePercentage(self, cards):

        rankingMap = self.getRankingMap()
        ranking = self.getRanking(cards, rankingMap)

        return ranking

    def getRankingMap(self):
        # load csv
        # parse csv to map & return

        filepath = '../resources/preflop-table.csv'

        rankingMap = {}

        with open(filepath, mode='r') as f:
            data = f.read().splitlines()
            for row in data:
                parts = row.split(';')

                valueOne = parts[0]
                valueTwo = parts[1]
                score = parts[2]

                representationOne = str(valueOne) + '-' + str(valueTwo)
                representationTwo = str(valueTwo) + '-' + str(valueOne)

                rankingMap[representationOne] = score
                rankingMap[representationTwo] = score

        return rankingMap
