from main import Deck, Hand


class Game:
    """ Here we wrote the logic that enable the player and dealer to determine who wins
    the game depending on the cards they are holding at each time the cards are shuffled."""

    def __init__(self) -> None:
        pass

    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            print("continue the game")
            try:
                games_to_play = int(
                    input("Enter how many games do you want to play? "))
            except:
                print("Kindly input a number not word")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game { game_number } of { games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(dealer_hand, player_hand):
                continue

            choice = " "
            while player_hand.get_value() < 21 and \
                    choice not in ['s', 'stand']:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()

                while choice not in ['h', 's', 'hit', 'stand']:
                    choice = input(
                        "Please enter 'Hit' or 'Stand' (or H/S): ").lower()
                    print()

                if choice in ['hit', 'h']:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(dealer_hand, player_hand):
                continue

            # store the value of each of their cards
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            """ continue to draw card (by dealer) until it's rank-value is more than 17"""
            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(dealer_hand, player_hand):
                continue

            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer hand:", dealer_hand_value)

            self.check_winner(dealer_hand, player_hand, True)

        print("\n Thanks for playing!")

    def check_winner(self, dealer_hand, player_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You bursted, dealer win! ☕")
                return True

            elif dealer_hand.get_value() > 21:
                print("Dealer bursted. You win! ❤️")
                return True

            elif dealer_hand.is_blackjack() and \
                    player_hand.is_blackjack():
                print("Both players have blackjack! Tie ")
                return True

            elif player_hand.is_blackjack():
                print("You have a blackjack. You win! ❤️")
                return True

            elif dealer_hand.is_blackjack():
                print("Dealer have a blackjack. Dealer Wins. You are bursted, dude! ")
                return True

        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print('You win! ❤️')

            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a Tie")

            else:
                print('Dealer win! ')

            return True
        return False


game1 = Game()
