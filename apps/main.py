
import random

""" CLASSES => provides a way of bundling data and functionality together. 

"""

class Deck:
    def __init__(self):
        
        self.cards = []

        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            
                    {"rank": "A", "value": 11},
                    {"rank": "2", "value": 2},
                    {"rank": "3", "value": 3},
                    {"rank": "4", "value": 4},
                    {"rank": "5", "value": 5},
                    {"rank": "6", "value": 6},
                    {"rank": "7", "value": 7},
                    {"rank": "8", "value": 8},
                    {"rank": "9", "value": 9},
                    {"rank": "10", "value": 10},
                    {"rank": "J", "value": 10},
                    {"rank": "Q", "value": 10},
                    {"rank": "K", "value": 10},
                    
            ]


        for suit in suits:
            """ do another loop for ranks """
            for rank in ranks:

                self.cards.append(Card(suit, rank)) # pass Card instances
        
                
    def shuffle(self):
        """Shuffle function. A deck with only one card does not need to be shuffled """
        if len(self.cards) > 0:
            random.shuffle(self.cards)
            return self.cards


    def deal(self,number):
        """ Removed item from the list of shuffled cards """
        
        card_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                card_dealt.append(card)
            
        return card_dealt

class Card:
    def __init__(self, suit, rank) :
        self.suit = suit
        self.rank = rank
    
    def __str__(self) :
        return f"{self.rank['rank']} of {self.suit}"
    
class Hand:
    """ Here, we handle dealer and computer control player throughout of 
    game."""
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0 
        self.dealer = dealer
        
        
    def add_card(self, card_list):
        self.cards.extend(card_list)
        return self.cards
    
    def calculate_value(self):
        self.value = 0
        self.has_ace = False
        for card in self.cards:
            card_value = int(card.rank['value'])
            self.value += card_value # 11 or 1
            
            if card.rank['rank'] == "Ace":
                self.has_ace = True
            
        if self.has_ace and self.value > 21:
            self.value -= 10 # subtract 10 from the value
            
    def get_value(self):
        """ retrieve each value from the hand when called """
        self.calculate_value()
        return self.value
        
    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self, show_all_dealer_card=False):
        print(f""" {"Dealer's" if self.dealer else "Your"} hand:""")
        
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_card\
                and not self.is_blackjack:
                return "hidden"
            
            print(index, card)
            
        if not self.dealer:
             print("Value:", self.get_value())
            


















            
            

        
        


