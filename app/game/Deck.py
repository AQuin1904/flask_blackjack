# flask_blackjack/app/game/Deck.py
from random import shuffle
from .Card import Card

class Deck:
    '''
    A class that represents a standard deck of 52 playing cards (no jokers)

    Attributes
    ----------
    cards: list of Card objects (namedtuples of the form [rank, suit])
        The remaining cards in the Deck
        ranks are ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king
        suits are hearts, clubs, diamonds, spades

    Methods
    -------
    draw():
        Repopulates and shuffles the deck if empty,
        then removes and returns the top card from the deck
    __build_deck():
        Generates a new, shuffled deck of 52 cards
        By default, called automatically only when the deck is empty
    '''
    __ranks__ = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
    __suits__ = ['hearts', 'clubs', 'diamonds', 'spades']

    def __init__(self, cards=None):
        '''
        Constructs the necessary attributes of a Deck object

        Parameters
        ----------
        cards=none: list of Card objects
            The current cards in the deck, ordered
            (used to begin with a specific subset or order of cards)
        '''
        if cards:
            self.cards = cards
        else:
            self.__build_deck()

    def draw(self):
        '''
        Repopulates and shuffles the deck if empty,
        then removes and returns the top card from the deck
        '''
        if len(self.cards) <= 0:
            self.__build_deck()
        return self.cards.pop()

    def __build_deck(self):
        '''
        Generates a new, shuffled deck of 52 cards
        By default, called automatically only when the deck is empty
        '''
        self.cards = [Card(rank, suit) for rank in self.__ranks__
                                       for suit in self.__suits__]
        shuffle(self.cards)
