class CardTransformer:

    rankMap = {
        'king': 'K',
        'queen': 'Q',
        'jack': 'J',
        'ten': 'T',
        'nine': '9',
        'eight': '8',
        'seven': '7',
        'six': '6',
        'five': '5',
        'four': '4',
        'three': '3',
        'two': '2',
        'one': '1'
    }

    suitMap = {
        'clubs': 'c',
        'spades': 's',
        'hearts': 'h',
        'diamonds': 'd'
    }

    def transformCard(self, card):
        rank = card['rank']
        suit = card['suit']

        newRank = CardTransformer.rankMap[rank]
        newSuit = CardTransformer.suitMap[suit]

        return '' + str(newRank) + str(newSuit)

    def transformCards(self, cards):
        transformed = []

        for item in cards:

            transf = self.translateCard(item)
            transformed.append(transf)

        return transformed
