class GameInfo:
    def __init__(self, gameInfo):
        self.gameInfo = gameInfo

    def getCards(self):
        return self.gameInfo["tableCards"]

    def getRoundTurn(self):
        return self.gameInfo["roundTurn"]

    def getTableCards(self):
        return self.gameInfo["tableCards"]

    def getMyCards(self):
        return self.gameInfo["yourCards"]

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
