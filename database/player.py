from database.database import get_session, Player


def get_user_by_user_id(user_id: int):
    return get_session().query(Player).filter(Player.TelegramID == user_id).one_or_none()


def get_user_by_xbox_id(xbox_id: int):
    return get_session().query(Player).filter(Player.XBoxID == xbox_id).one_or_none()
