from random import randint
from deuces import Evaluator
from mapper import Mapper


class Strategy():
    """
    TODO
    Add documentation

    """
    @staticmethod
    def decide_action(game_info, strategy):
        if game_info["roundTurn"] == 'pre_flop':
            hand = Strategy.evaluate_pre_flop_hand(game_info)
            action = Strategy.decide_action_pre_flop(game_info, strategy, hand)
        else:
            hand_evaluation = Strategy.evaluate_hand_given_table(game_info)
            return Strategy.decide_action_post_pre_flop(game_info, strategy, hand_evaluation)

        if action == 'bet':
            bet_chips = Strategy.calculate_bet_given_bet_factor(game_info, strategy[2])
            return {"action": "bet", "chips": bet_chips}

        if action == 'raise':
            bet_chips = Strategy.calculate_bet_given_bet_factor(game_info, strategy[2])
            return {"action": "raise", "chips": bet_chips}

        elif action == 'check':
            return {"action": "check"}

        elif action == 'call':
            return {"action": "call"}

        return {"action": "fold"}

    @staticmethod
    def evaluate_pre_flop_hand(game_info):
        cards_dict = game_info["yourCards"]
        cards_dict[0]['rank'] = Mapper.map_card_to_number(cards_dict[0]['rank'])
        cards_dict[1]['rank'] = Mapper.map_card_to_number(cards_dict[1]['rank'])
        print('\n' + str(cards_dict))

        hand = {'value': 7, 'run': False, 'same_suit': False}

        if cards_dict[0]['rank'] == cards_dict[1]['rank']:
            # AA
            if cards_dict[0]['rank'] == 14:
                hand['value'] = 1
            # KK / QQ / JJ
            elif cards_dict[0]['rank'] >= 11:
                hand['value'] = 2
            # Low Pair
            else:
                hand['value'] = 3

        else:
            high_card = max(cards_dict[0]['rank'], cards_dict[1]['rank'])
            low_card = min(cards_dict[0]['rank'], cards_dict[1]['rank'])

            if cards_dict[0]['suit'] == cards_dict[1]['suit']:
                hand['same_suit'] = True

            if high_card - low_card == 1:
                hand['run'] = True

            if high_card == 14:
                # AK / AQ / AJ
                if low_card >= 11:
                    hand['value'] = 4
                # A + low card
                hand['value'] = 5

            # KQ / KJ / QJ
            elif high_card > 10 and low_card > 10:
                hand['value'] = 6

        return hand

    @staticmethod
    def evaluate_hand_given_table(game_info):
        evaluator = Evaluator()

        hand = Mapper.map_card_to_evaluation_format(game_info["yourCards"])
        board = Mapper.map_card_to_evaluation_format(game_info["tableCards"])

        hand_score = evaluator.evaluate(board, hand)
        hand_class = evaluator.get_rank_class(hand_score)
        hand_type = evaluator.class_to_string(hand_class)

        print('|------ Hand score: ' + str(hand_score))
        print('|------ Hand class: ' + str(hand_class))
        print('|------ Hand type: ' + hand_type)
        return hand_class

    @staticmethod
    def decide_action_pre_flop(game_info, strategy, hand):
        hand_value = hand['value']
        hand_same_suit = hand['same_suit']
        hand_run = hand['run']

        aggressive_factor = strategy[0]
        if aggressive_factor == '5':
            if game_info["canCheckOrBet"]:
                if hand_value <= 6:
                    return 'bet'
                return 'check'
            elif game_info["canCallOrRaise"]:
                if hand_value <= 2:
                    return 'raise'
                elif hand_value < 7 or hand_same_suit or hand_run:
                    return 'call'
            return 'fold'

        elif aggressive_factor == '4':
            if game_info["canCheckOrBet"]:
                if hand_value <= 6:
                    return 'bet'
                return 'check'
            elif game_info["canCallOrRaise"]:
                if hand_value <= 2:
                    return 'raise'
                elif hand_value <= 5 or hand_same_suit:
                    return 'call'
            return 'fold'

        elif aggressive_factor == '3':

            if game_info["canCheckOrBet"]:
                if hand_value <= 4:
                    return 'bet'
                return 'check'
            elif game_info["canCallOrRaise"]:
                if hand_value <= 2:
                    return 'raise'
                elif hand_value <= 4 or (hand_same_suit and hand_run):
                    return 'call'
            return 'fold'

        elif aggressive_factor == '2':
            if game_info["canCheckOrBet"]:
                if hand_value <= 3:
                    return 'bet'
                return 'check'
            elif game_info["canCallOrRaise"]:
                if hand_value <= 2:
                    return 'call'
            return 'fold'

        elif aggressive_factor == '1':
            if game_info["canCheckOrBet"]:
                if hand_value <= 2:
                    return 'bet'
                return 'check'
            elif game_info["canCallOrRaise"]:
                if hand_value <= 2:
                    return 'call'
            return 'fold'

    @staticmethod
    def decide_action_post_pre_flop(game_info, strategy, hand_evaluation):
        aggressive_factor = int(strategy[0])
        bluff_factor = int(strategy[1])
        bet_factor = int(strategy[2])

        if game_info["canCheckOrBet"]:
            if hand_evaluation == 9 and aggressive_factor < 4:
                return {'action': 'check'}
            else:
                return {'action': 'raise', 'chips': min(game_info['minBet'] * (10 - hand_evaluation), game_info['yourChips'])}

        elif game_info["canCallOrRaise"]:
            your_chips_for_raise = game_info['yourChips'] - game_info['chipsToCall']

            # STRAIGHT FLUSH, 4 OF KIND, FUll HOUSE
            if hand_evaluation <= 3:
                if bet_factor > 4:
                    return {'action': 'raise', 'chips': game_info['yourChips']}
                else:
                    return {'action': 'raise', 'chips': min(game_info['minRaise'] + bet_factor + 3, your_chips_for_raise)}

            # STRAIGHT, FLUSH
            elif hand_evaluation <= 5:
                return {'action': 'raise', 'chips': min(game_info['minRaise'] + bet_factor + 2, your_chips_for_raise)}

            # 3 OF A KIND
            elif hand_evaluation == 6:
                bluff_action = Strategy.define_action_for_bluff(game_info, bluff_factor)
                if bluff_action is not None:
                    return bluff_action

                if bet_factor == 1:
                    return {'action': 'call'}
                else:
                    return {'action': 'raise', 'chips': min(game_info['minRaise'] + bet_factor + 1, your_chips_for_raise)}

            # 2 PAIRS
            elif hand_evaluation == 7:
                bluff_action = Strategy.define_action_for_bluff(game_info, bluff_factor)
                if bluff_action is not None:
                    return bluff_action

                if aggressive_factor == 1:
                    return {'action': 'fold'}
                elif bet_factor == 1:
                    return {'action': 'call'}
                else:
                    return {'action': 'raise', 'chips': min(game_info['minRaise'] + bet_factor, your_chips_for_raise)}

            # PAIR, HIGH CARD
            elif hand_evaluation <= 9:
                bluff_action = Strategy.define_action_for_bluff(game_info, bluff_factor)
                if bluff_action is not None:
                    return bluff_action

                if aggressive_factor < 4:
                    return {'action': 'fold'}
                else:
                    return {'action': 'call'}

        return {'action': 'call'}

    @staticmethod
    def define_action_for_bluff(game_info, bluff_factor):
        bluff_probability = bluff_factor * 10
        random_number = randint(1, 100)

        if random_number <= bluff_probability:
            random_bluff = randint(1, 20)

            # TODO DEFINE BLUFFING WEIGHTS
            your_chips_for_raise = game_info['yourChips'] - game_info['chipsToCall']
            if random_bluff > 15:
                return {'action': 'raise', 'chips': your_chips_for_raise}
            elif random_bluff > 10:
                return {'action': 'raise', 'chips': min(game_info['minRaise'] * 10, your_chips_for_raise)}

        return None

    @staticmethod
    def calculate_bet_given_bet_factor(game_info, bet_factor):
        if game_info["canCheckOrBet"]:
            bet_allowed = int(bet_factor) * game_info["minBet"] < game_info["yourChips"]
            if bet_allowed:
                return int(bet_factor) * game_info["minBet"]
            else:
                print('|------ Action: All-in')
                return game_info["yourChips"]

        elif game_info["canCallOrRaise"]:
            if game_info['chipsToCall'] >= game_info["yourChips"]:
                print('|------ Action: All-in')
                return game_info['chipsToCall']
            else:
                return int(bet_factor) * game_info["minRaise"]
