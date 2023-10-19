from main import Deck, Hand

class Game:
    
    def __init__(self):
        pass
    
    def play(self):
        try:
            game_number = 0
            games_to_play = 0
            
            while games_to_play <= 0:
                try:
                 games_to_play = int(input("Enter how many card do you want to play?"))
                
                except:
                    print("You must enter a number.")
                   
            print("We got your number correctly, kindly continue the game")

            while game_number < games_to_play:
                game_number += 1
                
                deck = Deck()
                deck.shuffle()
                
                player_hand = Hand()
                dealer_hand = Hand(dealer=True)
                
                for index in range(2):
                   player_hand.add_card(deck.deal(1))
                   dealer_hand.add_card(deck.deal(1))
                   
                   print()
                   print("*" *  30)
                   
                   print(f'Game {game_number} of {games_to_play}')
                   print("*" *  30)
                   
                   player_hand.display()
                   dealer_hand.display()
                   
                   if self.check_winner(dealer_hand, player_hand):
                        continue   # goes to the beginning of the loop...
                    
                   choice = ''
                   while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                       choice = input("Please choose 'Hit' or 'Stand: ").lower()
                       print()
                       
                       while choice not in ["h", "s", "hit", "stand"]:
                           choice = input("Please enter 'Ht' or 'Stand' {or H/S} ") \
                                        .lower()
                       if choice in ["hit", "h"]:
                            player_hand.add_card(deck.deal(1))
                            player_hand.display()  
                    
                   if self.check_winner(dealer_hand, player_hand):
                        continue   # goes to the beginning of the loop...
                   
                   dealer_hand_value = dealer_hand.get_value()     
                   player_hand_value = player_hand.get_value()     

                   while dealer_hand_value < 17:
                       dealer_hand.add_card(deck.deal(1))
                       dealer_hand_value = dealer_hand.get_value()
                    
                    # show all cards since it is the end of the game.
                   dealer_hand.display(show_all_dealer_card=True)
                
                # check for the winner just like befpre
                if self.check_winner(dealer_hand=dealer_hand, player_hand=player_hand):
                        continue   # goes to the beginning of the loop...
                 
                print("Final Results")
                print('Your hand:', player_hand_value)
                print('Dealer hand:', dealer_hand_value)
                
                
                # call check_winner function to state the game is over
                self.check_winner(player_hand, dealer_hand, True)
            print("\nThanks for playing.")
        except Exception as e:
            data = {e: "Value must be an integer. Kindly provide a number say 4 for example!"}
            print(data[e])
            
            
    def check_winner(self, dealer_hand, player_hand, game_over= False):
        """ check winner function of the game and know when game is over or not. """
        if not game_over: 
         
            if player_hand.get_value() > 21:
                print("You bursted, dealer win.😂")
                return True
            
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win!👏👏")
                
            elif player_hand.is_blackjack() == dealer_hand.is_blackjack():
                print("It's a tie, both players have a blackjack.😒")
                return True
            
            elif player_hand.is_blackjack():
                print("Whohoo! You have a blackjack, you win! 👏👏")
                return True
            
            elif dealer_hand.is_blackjack():
                print("Whohoo! Dealer have a blackjack, you lose! 👏👏")
                return True
        
            """ The game can also end if both players decide not to get more cards """
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!👏👏")
            elif player_hand.is_blackjack() == dealer_hand.is_blackjack():
                print("It's a tie! 😒")
            else: 
                print("Dealer wins. 😍")
            return True
        return False
        