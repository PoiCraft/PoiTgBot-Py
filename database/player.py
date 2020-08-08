from database.database import get_session, Player


def get_player_by_player_id(user_id: int):
    return get_session().query(Player).filter(Player.id == user_id).one_or_none()


def get_player_by_xbox_id(xbox_id: int):
    return get_session().query(Player).filter(Player.xbox_id == xbox_id).one_or_none()
