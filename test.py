import unittest
from Deck import Deck
from Player import Player
from Blackjack import Blackjack

class TestDeck(unittest.TestCase):
    ranks = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
    suits = ['hearts', 'clubs', 'diamonds', 'spades']
    def test_deck(self):
        d = Deck()
        self.assertEqual(len(d.cards), 52)
        for rank in self.ranks:
            self.assertEqual(sum((c.rank == rank) for c in d.cards), 4)
        for suit in self.suits:
            self.assertEqual(sum((c.suit == suit) for c in d.cards), 13)
        d = Deck([Deck.Card('ace', 'hearts')])
        self.assertEqual(len(d.cards), 1)

    def test_draw(self):
        d = Deck()
        for i in range(52, -1, -1):
            self.assertEqual(len(d.cards), i)
            self.assertEqual(len(d.draw()), 2)
        self.assertEqual(len(d.cards), 51)
        # Only a new deck object holds 52 cards
        self.assertEqual(len(d.draw()), 2)
        d = Deck([Deck.Card('ace', 'hearts'), Deck.Card('king', 'clubs')])
        c = d.draw()
        self.assertTrue(c.rank == 'king' and c.suit == 'clubs')

class TestPlayer(unittest.TestCase):
    def test_player(self):
        p = Player()
        self.assertEqual(len(p.hand), 0)
        self.assertEqual(p.total, 0)
        self.assertEqual(p.stand, False)
        p = Player([Deck.Card('ace', 'hearts')], 11, True)
        self.assertEqual(len(p.hand), 1)
        self.assertEqual(p.total, 11)
        self.assertEqual(p.stand, True)

class TestBlackjack(unittest.TestCase):
    def test_blackjack(self):
        bj = Blackjack()
        self.assertTrue(True)

    def test_total_hand(self):
        bj = Blackjack()
        self.assertTrue(True)

    def test_deal(self):
        bj = Blackjack()
        self.assertTrue(True)

    def test_hit(self):
        bj = Blackjack()
        self.assertTrue(True)

    def test_dealer_act(self):
        bj = Blackjack()
        self.assertTrue(True)

    def test_check_winner(self):
        bj = Blackjack()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
