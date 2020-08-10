from Deck import Deck
from Blackjack import Blackjack

d = Deck()
d.shuffle()
for x in range(0, 53):
    print(d.draw(), len(d.cards))

b = Blackjack()
print(b.com_hand, b.player_hand)
print(type(b), type(b.deck))
b.deal()
print(b.com_hand, b.player_hand)
