from api_client import vote

def submit_vote(poll_id, user_id, option):
    result = vote(poll_id, user_id, option)
    return result
