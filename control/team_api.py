from sqlalchemy.orm.exc import NoResultFound

from database.database import get_session, Player, Team


def create_team(leaderID: int):
    try:
        session = get_session()
        new_team = Team(leaderID=leaderID)
        session.add(new_team)
        player = session.query(Player).filter(Player.TelegramID == leaderID).one()
        player.TeamIN = new_team
        session.commit()
        session.close()
        return True
    except NoResultFound:
        return False


def join_team(userID: int, teamID: int = None, leaderID: int = None):
    try:
        session = get_session()
        if teamID is not None:
            team = session.query(Team).filter(Team.ID == teamID).one()
        elif leaderID is not None:
            team = session.query(Player).filter(Player.TelegramID == leaderID).one().TeamIN
        player = session.query(Player).filter(Player.TelegramID == userID).one()
        player.TeamIN = team
        session.commit()
        session.close()
        return True
    except NoResultFound:
        return False


def leave_team(userID: int):
    try:
        session = get_session()
        session.query(Player).filter(Player.TelegramID == userID).one().TeamIN = None
        session.commit()
        session.close()
        return True
    except NoResultFound:
        return False
