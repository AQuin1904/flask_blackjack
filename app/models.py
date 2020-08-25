# flask_blackjack/app/models.py
from sqlalchemy import Column, String, Integer, Boolean
from .database import Base

class BlackjackGame(Base):
    __tablename__ = 'blackjack_games'

    id = Column(String, primary_key=True)
    deck = Column(String)
    p_hand = Column(String)
    p_total = Column(Integer)
    p_stand = Column(Boolean)
    d_hand = Column(String)
    d_total = Column(Integer)
    d_stand = Column(Boolean)
