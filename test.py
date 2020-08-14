from Deck import Deck
from Blackjack import Blackjack

d = Deck()
d.shuffle()
for x in range(0, 53):
    print(d.draw(), len(d.cards))

b = Blackjack()
print(b.dealer.hand, b.player.hand)
print(b.dealer.total, b.player.total)
print(type(b), type(b.deck))
b.deal()
print(b.dealer.hand, b.player.hand)
print(b.dealer.total, b.player.total)
b.hit(b.dealer)
b.hit(b.player)
print(b.dealer.hand, b.player.hand)
print(b.dealer.total, b.player.total)
