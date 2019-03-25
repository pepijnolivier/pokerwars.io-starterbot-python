from src.utils.CardTransformer import CardTransformer


class GameInfo:
    def __init__(self, gameInfo):
        self.gameInfo = gameInfo
        self.cardTransformer = CardTransformer()

    def getCards(self):
        return self.gameInfo["tableCards"]

    def getRoundTurn(self):
        return self.gameInfo["roundTurn"]

    def getTableCards(self):
        cards = self.gameInfo["tableCards"]
        return self.cardTransformer.transformCards(cards)

    def getMyCards(self):
        cards = self.gameInfo["yourCards"]
        return self.cardTransformer.transformCards(cards)

    def getTournamentId(self):
        return self.gameInfo["tournamentId"]

    def canCheckOrBet(self):
        return self.gameInfo["canCheckOrBet"]

    def canCallOrRaise(self):
        return self.gameInfo["canCallOrRaise"]

    def getChipsToCall(self):
        if(self.canCallOrRaise() == False):
            return 0

        return self.gameInfo["chipsToCall"]

    def getMinRaise(self):
        return self.gameInfo["minRaise"]
