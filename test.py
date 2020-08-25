import unittest
from app.game.Deck import Deck
from app.game.Player import Player
from app.game.Blackjack import Blackjack
from app.game.Card import Card

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.d = Deck()

    def test_deck(self):
        self.assertEqual(len(self.d.cards), 52)
        for rank in Deck.__ranks__:
            self.assertEqual(sum((c.rank == rank) for c in self.d.cards), 4)
        for suit in Deck.__suits__:
            self.assertEqual(sum((c.suit == suit) for c in self.d.cards), 13)
        self.d = Deck([Card('ace', 'hearts')])
        self.assertEqual(len(self.d.cards), 1)

    def test_draw(self):
        d = Deck()
        for i in range(52, -1, -1):
            self.assertEqual(len(d.cards), i)
            self.assertEqual(len(d.draw()), 2)
        self.assertEqual(len(d.cards), 51)
        # Only a new deck object holds 52 cards
        self.assertEqual(len(d.draw()), 2)
        d = Deck([Card('ace', 'hearts'), Card('king', 'clubs')])
        c = d.draw()
        self.assertTrue(c.rank == 'king' and c.suit == 'clubs')

    def tearDown(self):
        del self.d

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.p = Player()

    def test_player(self):
        self.assertEqual(len(self.p.hand), 0)
        self.assertEqual(self.p.total, 0)
        self.assertEqual(self.p.stand, False)
        self.p = Player([Card('ace', 'hearts')], 11, True)
        self.assertEqual(len(self.p.hand), 1)
        self.assertEqual(self.p.total, 11)
        self.assertEqual(self.p.stand, True)

    def tearDown(self):
        del self.p

class TestBlackjack(unittest.TestCase):
    def setUp(self):
        self.bj = Blackjack()

    def test_blackjack(self):
        self.assertEqual(len(self.bj.deck.cards), 52)
        self.assertEqual(len(self.bj.player.hand), 0)
        self.assertEqual(len(self.bj.dealer.hand), 0)
        self.assertEqual(self.bj.player.total, 0)
        self.assertEqual(self.bj.dealer.total, 0)
        self.assertFalse(self.bj.player.stand)
        self.assertFalse(self.bj.dealer.stand)
        self.bj = Blackjack(
                            p_hand=[Card('ace', 'hearts')],
                            p_total=11,
                            p_stand=True
                           )
        self.assertEqual(len(self.bj.player.hand), 1)
        self.assertEqual(len(self.bj.dealer.hand), 0)
        self.assertEqual(self.bj.player.total, 11)
        self.assertEqual(self.bj.dealer.total, 0)
        self.assertTrue(self.bj.player.stand)
        self.assertFalse(self.bj.dealer.stand)

    def test_total_hand(self):
        # Blackjack, 21
        hand_1 = [Card('ace', 'hearts'), Card('king', 'hearts')]
        # four aces, 14
        hand_2 = [
                  Card('ace', 'hearts'),
                  Card('ace', 'diamonds'),
                  Card('ace', 'clubs'),
                  Card('ace', 'spades'),
                 ]
        # four aces and a court card, 14
        hand_3 = [
                  Card('ace', 'hearts'),
                  Card('ace', 'diamonds'),
                  Card('ace', 'clubs'),
                  Card('ace', 'spades'),
                  Card('jack', 'diamonds')
                 ]
        # one whole suit, 85
        hand_4 = [
                  Card('ace', 'hearts'),
                  Card(2, 'hearts'),
                  Card(3, 'hearts'),
                  Card(4, 'hearts'),
                  Card(5, 'hearts'),
                  Card(6, 'hearts'),
                  Card(7, 'hearts'),
                  Card(8, 'hearts'),
                  Card(9, 'hearts'),
                  Card(10, 'hearts'),
                  Card('jack', 'hearts'),
                  Card('queen', 'hearts'),
                  Card('king', 'hearts'),
                 ]
        # an empty hand, 0
        hand_5 = []
        self.bj.player.hand = hand_1
        self.bj.total_hand(self.bj.player)
        self.assertEqual(self.bj.player.total, 21)
        self.bj.dealer.hand = hand_2
        self.bj.total_hand(self.bj.dealer)
        self.assertEqual(self.bj.dealer.total, 14)
        self.bj.player.hand = hand_3
        self.bj.total_hand(self.bj.player)
        self.assertEqual(self.bj.player.total, 14)
        self.bj.dealer.hand = hand_4
        self.bj.total_hand(self.bj.dealer)
        self.assertEqual(self.bj.dealer.total, 85)
        self.bj.player.hand = hand_5
        self.bj.total_hand(self.bj.player)
        self.assertEqual(self.bj.player.total, 0)

    def test_deal(self):
        self.bj.deal()
        self.assertEqual(len(self.bj.player.hand), 2)
        self.assertEqual(len(self.bj.dealer.hand), 2)
        # test that deal() properly resets players
        self.bj.hit(self.bj.player)
        self.bj.player.stand = True
        self.bj.deal()
        self.assertEqual(len(self.bj.player.hand), 2)
        self.assertEqual(len(self.bj.dealer.hand), 2)
        self.assertFalse(self.bj.player.stand)

    def test_hit(self):
        self.bj.hit(self.bj.player)
        self.assertEqual(len(self.bj.player.hand), 1)
        self.assertTrue(self.bj.player.total > 0)

    def test_dealer_act(self):
        # dealer hits if total < 17
        self.bj.dealer_act()
        self.assertEqual(len(self.bj.dealer.hand), 1)
        self.assertTrue(self.bj.dealer.total > 0)
        self.assertFalse(self.bj.dealer.stand)
        self.bj.dealer.total = 16
        self.bj.dealer_act()
        self.assertEqual(len(self.bj.dealer.hand), 2)
        # dealer stands if total >= 17
        self.bj.dealer.hand = []
        self.bj.dealer.total = 17
        self.bj.dealer_act()
        self.assertEqual(len(self.bj.dealer.hand), 0)
        self.assertEqual(self.bj.dealer.total, 17)
        self.assertTrue(self.bj.dealer.stand)

    def test_check_winner(self):
        # returns false if no winner
        self.assertFalse(self.bj.check_winner())
        # returns dealer if dealer has 21 or player busts
        self.bj.dealer.total = 21
        self.assertEqual(self.bj.check_winner(), self.bj.dealer)
        self.bj.dealer.total = 0
        self.bj.player.total = 22
        self.assertEqual(self.bj.check_winner(), self.bj.dealer)
        # returns player if player has 21 or dealer busts
        self.bj.dealer.total = 22
        self.bj.player.total = 0
        self.assertEqual(self.bj.check_winner(), self.bj.player)
        self.bj.dealer.total = 20
        self.bj.player.total = 21
        self.assertEqual(self.bj.check_winner(), self.bj.player)
        # returns false otherwise unless both players stand
        self.bj.player.stand = True
        self.bj.dealer.total = 15
        self.bj.player.total = 10
        self.assertFalse(self.bj.check_winner())
        # if both players stand, returns player whose total is greater
        self.bj.dealer.stand = True
        self.assertEqual(self.bj.check_winner(), self.bj.dealer)
        self.bj.dealer.total = 10
        self.bj.player.total = 15
        self.assertEqual(self.bj.check_winner(), self.bj.player)

    def tearDown(self):
        del self.bj

if __name__ == '__main__':
    unittest.main()
