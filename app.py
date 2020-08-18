from flask import Flask, render_template, request
from Blackjack import Blackjack
app = Flask(__name__)

bj = Blackjack()

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
    return render_template('play.html',
                           dealer_hand=bj.dealer.hand,
                           player_hand=bj.player.hand,
                           action=action
                          )
