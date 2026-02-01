from api_client import create_poll, get_poll

def start_poll(group_id, question, options, created_by):
    result = create_poll(group_id, question, options, created_by)
    return result

def fetch_poll(poll_id):
    return get_poll(poll_id)
