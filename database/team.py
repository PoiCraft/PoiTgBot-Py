from database.database import get_session, Team


def get_team_by_team_id(id: int):
    return get_session().query(Team).filter(Team.id == id).one_or_none()


def get_team_by_leader_id(id: int):
    return get_session().query(Team).filter(Team.leader_id == id).one_or_none()
