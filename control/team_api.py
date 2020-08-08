from sqlalchemy.orm.exc import NoResultFound

from database.database import get_session, Player, Team


def create_team(leaderID: int):
    try:
        session = get_session()
        new_team = Team(leader_id=leaderID)
        session.add(new_team)
        session.commit()
        player = session.query(Player).filter(Player.id == leaderID).one()
        player.team_id = new_team.id
        session.add(player)
        session.commit()
        session.close()
        return {'result': True, 'team_id': new_team.id}
    except NoResultFound:
        return {'result': False, 'team_id': None}


def join_team(userID: int, teamID: int = None, leaderID: int = None):
    try:
        session = get_session()
        if teamID is not None:
            team = session.query(Team).filter(Team.id == teamID).one()
        elif leaderID is not None:
            team = session.query(Team).filter(Team.leader_id == leaderID).one()
        player = session.query(Player).filter(Player.id == userID).one()
        player.team_id = team.id
        session.add(player)
        session.commit()
        session.close()
        return {'result': True, 'team_id': team.id}
    except NoResultFound:
        return {'result': False, 'team_id': None}


def leave_team(userID: int):
    try:
        session = get_session()
        player = session.query(Player).filter(Player.id == userID).one()
        team_id = player.team_id
        player.team_id = None
        session.add(player)
        session.commit()
        session.close()
        return {'result': True, 'team_id': team_id}
    except NoResultFound:
        return {'result': False, 'team_id': team_id}
