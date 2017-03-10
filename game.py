import string
import random
from cards import Card,Deck
class Player:
    def __init__(self,name):
        self.name = name
       
class Game:
    def __init__(self,players):
        self.players = players
        self.deck = Deck()
        self.player_cards = dict()
    
    def assign_card_to_player(self):
         for player in self.players:
             card =  self.deck.draw_random_card()
             self.player_cards[player] = card
             print "player " + player.name + " got " + str(card)

    def decide_winner(self):
         w_card = None
         w_player = None
         val = 0
         for player,card in self.player_cards.iteritems():
             if card.value > val:
                 w_player = player
                 w_card = card
                 val = card.value
         return (w_player,w_card)


player1 = Player("abc") 
player2 = Player("xyz")
players = [player1,player2]

g = Game(players)
g.assign_card_to_player()
(player,card) = g.decide_winner()
print "winning player is " + player.name + " and card is " + str(card)

