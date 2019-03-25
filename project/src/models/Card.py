class Card:
    def __init__(self, card):
        # id, suit, value
        self.card = card

    def getId(self):
        return self.card.id

    def getSuit(self):
        return self.card.suit

    def getValue(self):
        return self.card.value
