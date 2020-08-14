from flask import Flask, render_template
from Blackjack import Blackjack
app = Flask(__name__)

def game():
    bj = Blackjack()
    yield bj
    bj.deal()
    yield bj

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    bj = next(game())
    return render_template('play.html',
                           dealer_hand=bj.dealer.hand,
                           player_hand=bj.player.hand,
                           action='deal'
                          )
