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
    if next == '':
        action = 'deal'
    elif next == 'deal':
        bj.deal()
        action = 'hit'
    elif next == 'hit':
        bj.hit(bj.player)
        action = 'hit'
    else:
        action = 'hit'
    return render_template('play.html',
                           dealer_hand=bj.dealer.hand,
                           player_hand=bj.player.hand,
                           action=action
                          )
