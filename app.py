from flask import Flask, render_template, request
from Blackjack import Blackjack
app = Flask(__name__)

bj = Blackjack()

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    global bj
    next = request.args.get('next', '')
    action_t = '<a href="/play?next={act}">{act}</a>'
    if next == '':
        action = action_t.format(act='deal')
    elif next == 'deal':
        bj.deal()
        action = (action_t.format(act='hit')
                 + action_t.format(act='stand'))
    elif next == 'hit':
        bj.dealer_act()
        bj.hit(bj.player)
        action = (action_t.format(act='hit')
                 + action_t.format(act='stand'))
    elif next == 'stand':
        bj.dealer_act()
        bj.player.stand = True
        action = action_t.format(act='stand')
    else:
        action = (action_t.format(act='hit')
                 + action_t.format(act='stand'))

    winner = bj.check_winner()
    if winner == bj.dealer:
        action = ('<h3>Dealer wins!<br>Play again?</h3>'
                 + action_t.format(act='deal'))
    elif winner == bj.player:
        action = ('<h3>You win!<br>Play again?</h3>'
                 + action_t.format(act='deal'))

    dealer_hand, player_hand=cards_to_display(bj.dealer, bj.player, winner)
    return render_template('play.html',
                           dealer_hand=dealer_hand,
                           player_hand=player_hand,
                           action=action
                          )
