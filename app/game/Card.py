# flask_blackjack/app/game/Card.py
from collections import namedtuple

'''
A namedtuple representing a standard playing card

Attributes
----------
rank: str or int
    The card's rank
    (ace, jack, queen, and king are strings; all other ranks are ints)
suit: str
    The card's suit
'''
Card = namedtuple('Card', ['rank', 'suit'])
