import requests
from config import WORKER_API_URL

def add_user(telegram_id, username, role="normal"):
    url = f"{WORKER_API_URL}/add_user"
    resp = requests.post(url, json={"telegram_id": telegram_id, "username": username, "role": role})
    return resp.json()

def create_poll(group_id, question, options, created_by):
    url = f"{WORKER_API_URL}/create_poll"
    resp = requests.post(url, json={
        "group_id": group_id,
        "question": question,
        "options": options,
        "created_by": created_by
    })
    return resp.json()

def vote(poll_id, user_id, option):
    url = f"{WORKER_API_URL}/vote"
    resp = requests.post(url, json={"poll_id": poll_id, "user_id": user_id, "option": option})
    return resp.json()

def get_poll(poll_id):
    url = f"{WORKER_API_URL}/poll/{poll_id}"
    resp = requests.get(url)
    return resp.json()
