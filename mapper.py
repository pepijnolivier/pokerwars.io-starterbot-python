from deuces.card import Card


class Mapper:
    """
    Todo
    Add documentation

    """
    @staticmethod
    def map_card_to_number(x):
        x_low = x.lower()
        if x_low == 'deuce':
            return 2
        elif x_low == 'three':
            return 3
        elif x_low == 'four':
            return 4
        elif x_low == 'five':
            return 5
        elif x_low == 'six':
            return 6
        elif x_low == 'seven':
            return 7
        elif x_low == 'eight':
            return 8
        elif x_low == 'nine':
            return 9
        elif x_low == 'ten':
            return 10
        elif x_low == 'jack':
            return 11
        elif x_low == 'queen':
            return 12
        elif x_low == 'king':
            return 13
        elif x_low == 'ace':
            return 14
        else:
            print('Error --> map_card_to_number')
            return -1

    @staticmethod
    def map_card_to_evaluation_format(cards):
        formatted_cards = []
        for card in cards:
            rank = card["rank"]
            rank = rank.lower()
            if rank == 'deuce':
                output = '2'
            elif rank == 'three':
                output = '3'
            elif rank == 'four':
                output = '4'
            elif rank == 'five':
                output = '5'
            elif rank == 'six':
                output = '6'
            elif rank == 'seven':
                output = '7'
            elif rank == 'eight':
                output = '8'
            elif rank == 'nine':
                output = '9'
            elif rank == 'ten':
                output = 'T'
            elif rank == 'jack':
                output = 'J'
            elif rank == 'queen':
                output = 'Q'
            elif rank == 'king':
                output = 'K'
            elif rank == 'ace':
                output = 'A'
            else:
                print('Error --> map_card_to_evaluation_format')
                return -1

            suit = card["suit"]
            suit = suit.lower()
            if suit == 'hearts':
                output += 'h'
            elif suit == 'diamonds':
                output += 'd'
            elif suit == 'clubs':
                output += 'c'
            elif suit == 'spades':
                output += 's'
            else:
                print('Error --> map_card_to_evaluation_format')
                return -1

            formatted_cards.append(Card.new(output))

        return formatted_cards
