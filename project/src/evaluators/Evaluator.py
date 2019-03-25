from utils import CardTransformer
from PreFlopEvaluator import PreFlopEvaluator


class Evaluator:

    def __init__(self, gameInfo):
        self.gameInfo = gameInfo

        self.roundTurn = gameInfo.getRoundTurn()
        self.myCards = gameInfo.getMyCards()
        self.tableCards = gameInfo.getTableCards()

    # Always returns a percentage between 0 and 100.
    # 100 = perfect hand
    #   0 = weak hand
    def evaluate(self, evaluationStrategy):

        allCards = self.myCards + self.tableCards
        transformedCards = CardTransformer.transformCards(allCards)

        cardsCount = len(allCards)

        if(cardsCount === 2):
            # pre-flop > use map
            percentage = PreflopEvaluator.evaluatePercentage(transformedCards)
            return percentage

        else:
            # deuces evaluator
            percentage = DeucesEvaluator.evaluatePercentage(transformedCards)
            return percentage
