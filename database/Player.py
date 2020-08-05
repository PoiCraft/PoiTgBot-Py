from sqlalchemy import Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Player(Base):
    __tablename__ = 'player'
    TelegramID = Column(Integer, primary_key=True)
    XBoxID = Column(Text)
    TpNumber = Column(Integer)
