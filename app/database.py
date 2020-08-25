# flask_blackjack/app/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.environ.get('DATABASE_URL'))
Session = sessionmaker(engine)
Base = declarative_base()
