# flask_blackjack/app/game/Player.py
class Player:
    '''
    A class modeling a player in a game of Blackjack

    Attributes
    ----------
    hand: list of Card objects
        The player's hand of cards
    total: int
        The current value of the player's hand
    stand: bool
        Whether the player has chosen to stand in the current hand
    '''
    def __init__(self, hand=None, total=0, stand=False):
        '''
        Constructs the necessary attributes of a Player object
        (Use parameters only when reconstructing a game in progress)

        Parameters
        ----------
        hand=None: list of Card objects
            The player's hand of cards
        total=0: int
            The current value of the player's hand
        stand=False: bool
            Whether the player has chosen to stand in the current hand
        '''
        if hand == None:
            self.hand = []
        else:
            self.hand = hand
        self.total = total
        self.stand = stand
