# flask_blackjack/app/wsgi.py
from flask import Flask, session, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean
from uuid import uuid1
from json import dumps, loads
import os
from game.Blackjack import Blackjack
from game.Card import Card
from display import cards_to_display

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

db_string = os.environ.get('DATABASE_URL')
db = create_engine(db_string)
Session = sessionmaker(db)
db_session = Session()
base = declarative_base()
base.metadata.create_all(db)

class BlackjackGame(base):
    __tablename__ = 'blackjack_games'

    id = Column(String, primary_key=True)
    deck = Column(String)
    p_hand = Column(String)
    p_total = Column(Integer)
    p_stand = Column(Boolean)
    d_hand = Column(String)
    d_total = Column(Integer)
    d_stand = Column(Boolean)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    in_db = False
    if 'id' in session:
        game = (
                db_session
                .query(BlackjackGame)
                .filter(BlackjackGame.id == session['id'])
               )
        if game.count() > 0:
            game = game[0]
            bj = Blackjack(
                           cards=[Card(*c) for c in loads(game.deck)],
                           p_hand=[Card(*c) for c in loads(game.p_hand)],
                           p_total=game.p_total,
                           p_stand=game.p_stand,
                           d_hand=[Card(*c) for c in loads(game.d_hand)],
                           d_total=game.d_total,
                           d_stand=game.d_stand
                          )
            in_db = True
        else:
            bj = Blackjack()
    else:
        session['id'] = str(uuid1())
        bj = Blackjack()

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

    if in_db:
        game.deck = dumps(bj.deck.cards)
        game.p_hand = dumps(bj.player.hand)
        game.p_total = bj.player.total
        game.p_stand = bj.player.stand
        game.d_hand = dumps(bj.dealer.hand)
        game.d_total = bj.dealer.total
        game.d_stand = bj.dealer.stand
    else:
        game = BlackjackGame(
                             id=session['id'],
                             deck=dumps(bj.deck.cards),
                             p_hand=dumps(bj.player.hand),
                             p_total=bj.player.total,
                             p_stand=bj.player.stand,
                             d_hand=dumps(bj.dealer.hand),
                             d_total=bj.dealer.total,
                             d_stand=bj.dealer.stand
                            )
        db_session.add(game)
    db_session.commit()

    dealer_hand, player_hand=cards_to_display(bj.dealer, bj.player, winner)
    return render_template(
                           'play.html',
                           dealer_hand=dealer_hand,
                           player_hand=player_hand,
                           action=action
                          )

if __name__ == '__main__':
    app.run()
