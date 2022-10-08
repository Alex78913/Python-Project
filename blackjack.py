import random
import clear


class BlackJack:
    user_cards = []
    computer_cards = []
    is_game_over = False

    @staticmethod
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    @staticmethod
    def calculate_score(cards):
        return sum(cards)

    @staticmethod
    def compare(user_score, computer_score):
        pass


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            user_should_deal = input('write (y) to get another card, type (n) to pass: ')
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

