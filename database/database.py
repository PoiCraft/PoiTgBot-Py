from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

from config import DB_USER, DB_PASS, DB_HOST, DB_NAME

engine = create_engine(
    'mysql+pymysql://%s:%s@%s/%s' % (DB_USER, DB_PASS, DB_HOST, DB_NAME), echo=True)
base = declarative_base()
Session = sessionmaker(bind=engine)


class Player(base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    xbox_id = Column(Text)
    tp_number = Column(Integer)
    poi_coin = Column(Integer)
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship('Team', backref='members')


class Team(base):
    __tablename__ = 'team'
    id = Column(Integer, autoincrement=True, primary_key=True)
    leader_id = Column(Integer)


def create_db():
    base.metadata.create_all(engine)


def drop_db():
    base.metadata.drop_all(engine)


def get_session():
    session = scoped_session(Session)
    return session
