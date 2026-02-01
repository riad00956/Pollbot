from api_client import add_user

def add_group_admin(telegram_id, username):
    return add_user(telegram_id, username, role="group_admin")

def add_super_admin(telegram_id, username):
    return add_user(telegram_id, username, role="super_admin")
