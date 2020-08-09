from sqlalchemy.orm.exc import NoResultFound

from database.database import get_session, Player, Team
from database.team import get_team_by_leader_id, get_team_by_team_id
from database.player import get_player_by_player_id


def create_team(leaderID: int):
    try:
        session = get_session()
        new_team = Team(leader_id=leaderID)
        session.add(new_team)
        session.commit()
        player = get_player_by_player_id(leaderID)
        player.team_id = new_team.id
        session.commit()
        return {'result': True, 'team_id': new_team.id}
    except NoResultFound:
        return {'result': False, 'team_id': None}


def join_team(userID: int, teamID: int = None, leaderID: int = None):
    session = get_session()
    if teamID is not None:
        team = get_team_by_team_id(teamID)
    elif leaderID is not None:
        team = get_team_by_leader_id(leaderID)
    player = get_player_by_player_id(userID)
    if player is None or team is None:
        return {'result': False, 'team_id': None}
    player.team_id = team.id
    session.commit()
    return {'result': True, 'team_id': team.id}


def leave_team(userID: int):
    session = get_session()
    player = get_player_by_player_id(userID)
    team_id = player.team_id
    player.team_id = None
    session.commit()
    return {'result': True, 'team_id': team_id}
