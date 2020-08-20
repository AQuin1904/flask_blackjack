from Deck import Deck
from Player import Player

class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Player()

    def total_hand(self, player):
        ace_1 = 0
        ace_11 = 0
        new_total = 0
        for card in player.hand:
            if card.rank == 'ace':
                ace_1 += 1
                ace_11 += 11
            elif card.rank in ['jack', 'queen', 'king']:
                ace_1 += 10
                ace_11 += 10
            else:
                ace_1 += card.rank
                ace_11 += card.rank
        if ace_11 <= 21:
            player.total = ace_11
        else:
            player.total = ace_1


    def deal(self):
        self.player = Player()
        self.dealer = Player()
        self.dealer.hand.append(self.deck.draw())
        self.player.hand.append(self.deck.draw())
        self.dealer.hand.append(self.deck.draw())
        self.player.hand.append(self.deck.draw())
        self.total_hand(self.player)
        self.total_hand(self.dealer)

    def hit(self, player):
        player.hand.append(self.deck.draw())
        self.total_hand(player)

    def dealer_act(self):
        if self.dealer.total < 17:
            self.hit(self.dealer)
        else:
            self.dealer.stand = True

    def check_winner(self):
        if self.player.total > 21 or self.dealer.total == 21:
            return self.dealer
        elif self.dealer.total > 21 or self.player.total == 21:
            return self.player
        elif self.dealer.stand and self.player.stand:
            if self.dealer.total >= self.player.total:
                return self.dealer
            else:
                return self.player
        else:
            return False
