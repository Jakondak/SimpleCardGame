import random
class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def _convertToFaceValue(self,value):
        d = {1:"Ace",
             2:"Two",
             3:"Three",
             4:"Four",
             5:"Five",
             6:"Six",
             7:"Seven",
             8:"Eight",
             9:"Nine",
             10:"Ten",
             11:"Jack",
             12:"Queen",
             13:"King"
             }
        return d[value]
    def __str__(self):
         return self.suit + " " + self._convertToFaceValue(self.value)

class Deck:
    def __init__(self):
        self.suits = ["spade","club","diamond","heart"]
        self.values = range(1,14)
        self.cards = [];
        for suit in self.suits:
            for value in self.values:
                card = Card(suit,value)
                self.cards.append(card)

    def draw_random_card(self):
        card_no = random.randint(1,52)
        card = self.cards.pop(card_no)
        return card

    def shuffle_cards(self):
        print "going to shuffle cards"
        for i in range (1,52):
            s = random.randint(1,51)
            index = 51 % s
            (self.cards[i],self.cards[index] ) = (self.cards[index],self.cards[i])
            
    def display_cards(self,no=52):
        for card in self.cards[0:no]:
            print card
