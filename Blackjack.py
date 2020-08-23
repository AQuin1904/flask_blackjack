from Deck import Deck
from Player import Player

class Blackjack:
    '''
    A class for representing a game of Blackjack
    with one player and a computer-controlled dealer.

    Attributes
    ----------
    deck: Deck
        A standard deck of 52 playing cards
    player: Player
        The game's human player
    dealer: Player
        The game's dealer

    Methods
    -------
    total_hand(player):
        Sets a player's total based on their current hand
    deal():
        Starts a new hand and deals two cards into the hand of each player
    hit(player):
        Deals one card into a player's hand and updates their current total
    dealer_act():
        Determines and performs the dealer's next action (hit or stand)
    check_winner():
        Returns the winner of the game
        or False if the game is still in progress
    '''
    def __init__(self,
                 cards=None,
                 p_hand=[],
                 p_total=0,
                 p_stand=False,
                 d_hand=[],
                 d_total=0,
                 d_stand=False
                ):
        '''
        Constructs the necessary attributes of a Blackjack object
        (Only use parameters to restore a game in progress)

        Parameters
        ----------
        cards=None: list of Card objects
            The cards currently in the deck
        p_hand=[]: list of Card objects
            The player's hand
        p_total=0: int
            The player's total score
        p_stand=False: bool
            Whether the player has chosen to stand in the current hand
        d_hand=[]: list of Card objects
            The dealer's hand
        d_total=0: int
            The dealer's total score
        d_stand=False: bool
            Whether the dealer has chosen to stand in the current hand
        '''
        self.deck = Deck(cards)
        self.player = Player(p_hand, p_total, p_stand)
        self.dealer = Player(d_hand, d_total, d_stand)

    def total_hand(self, player):
        '''
        Sets a player's total score based on their current hand,
        using the optimal value for each ace

        Parameters
        ----------
        player: Player
            The player whose score is to be totalled
        '''
        total = 0
        ace_count = 0
        for card in player.hand:
            if card.rank == 'ace':
                total += 1
                ace_count += 1
            elif card.rank in ['jack', 'queen', 'king']:
                total += 10
            else:
                total += card.rank
        while ace_count > 0 and total <= 11:
            total += 10
        player.total = total


    def deal(self):
        '''
        Begins a new hand
        Resets all dealer and player attributes
        and deals two cards each to the dealer and player,
        beginning with the dealer and alternating,
        then updates dealer and player's total scores
        '''
        self.player = Player()
        self.dealer = Player()
        self.dealer.hand.append(self.deck.draw())
        self.player.hand.append(self.deck.draw())
        self.dealer.hand.append(self.deck.draw())
        self.player.hand.append(self.deck.draw())
        self.total_hand(self.player)
        self.total_hand(self.dealer)

    def hit(self, player):
        '''
        Draws a card from the deck and adds it to a player's hand,
        then updates that players total score to reflect their new hand

        Parameters
        ----------
        player: Player
            The player who is choosing to hit
        '''
        player.hand.append(self.deck.draw())
        self.total_hand(player)

    def dealer_act(self):
        '''
        Determines and executes the dealer's action for a turn
        Hits if the dealer's total score is 16 or less, stands otherwise
        '''
        if self.dealer.total < 17:
            self.hit(self.dealer)
        else:
            self.dealer.stand = True

    def check_winner(self):
        '''
        Returns the winner of the current hand if one exists
        Returns false otherwise
        '''
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
