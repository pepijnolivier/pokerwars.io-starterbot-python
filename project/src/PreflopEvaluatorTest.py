from evaluators.PreFlopEvaluator import PreFlopEvaluator
from models.Card import Card
from utils.AttributeDict import AttributeDict

cardTwo = Card(AttributeDict({
    'id': '9s',
    'suit': 'spades',
    'value': 9
}))

cardOne = Card(AttributeDict({
    'id': '8s',
    'suit': 'spades',
    'value': 8
}))

cards = [cardOne, cardTwo]

evaluator = PreFlopEvaluator()
percentage = evaluator.evaluatePercentage(cards)

print(percentage)
