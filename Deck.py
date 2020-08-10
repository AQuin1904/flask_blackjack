from collections import namedtuple
from random import shuffle

class Deck:
    Card = namedtuple('Card', ['rank', 'suit'])
    __ranks = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'king', 'queen']
    __suits = ['hearts', 'clubs', 'diamonds', 'spades']

    def __init__(self):
        self.cards = [self.Card(rank, suit) for rank in self.__ranks
                                            for suit in self.__suits]

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) <= 0:
            self.cards = [self.Card(rank, suit) for rank in self.__ranks
                                                for suit in self.__suits]
            self.shuffle()
        return self.cards.pop()
