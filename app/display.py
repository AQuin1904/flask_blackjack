# flask_blackjack/app/display.py
def cards_to_display(dealer, player, winner):
    card_t = ('<div class="card">{rank} of '
             + '<span class="{suit}">{suit}</span></div>')
    dealer_hand = ''
    player_hand = ''
    if len(dealer.hand) > 0 and not winner:
        dealer_hand += card_t.format(rank = '?', suit = '?')
        for card in dealer.hand[1:]:
            dealer_hand += card_t.format(rank = card.rank, suit = card.suit)
    else:
        for card in dealer.hand:
            dealer_hand += card_t.format(rank = card.rank, suit = card.suit)
    for card in player.hand:
        player_hand += card_t.format(rank = card.rank, suit = card.suit)
    return dealer_hand, player_hand
