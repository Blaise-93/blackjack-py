
import random
import utils
from utils import Card

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


class Hand:
    """ Here, we handle dealer and computer control player throughout of 
    game."""
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0 
        self.dealer = dealer
        
card = Card('hearts',   {"rank": "7", "value": 7})
print(card)