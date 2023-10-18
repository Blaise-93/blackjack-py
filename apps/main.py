import random

class Deck:
    """  """
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
                suit_rank_collection = [ suit, rank]
                self.cards.append(suit_rank_collection)
        
                
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards


    def deal(self,number):
        """ Removed item from the list of shuffled cards """
        
        card_dealt = []
        
        for x in range(number):
            card = self.cards.pop()
            card_dealt.append(card)
            
        return card_dealt


deck1 = Deck()
deck2 = Deck()

print(deck1.cards)

deck2.shuffle()

card2 = deck2.cards
print(card2)


        
        



