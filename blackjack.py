from Deck import Deck

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = []
        self.com_hand = []

    def deal(self):
        self.com_hand.append(self.deck.draw())
        self.player_hand.append(self.deck.draw())
        self.com_hand.append(self.deck.draw())
        self.player_hand.append(self.deck.draw())
