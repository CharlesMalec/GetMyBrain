import requests
import json
from datetime import datetime

# Trello API credentials (replace with your own)
API_KEY = "YOUR_API_KEY"
API_TOKEN = "YOUR_API_TOKEN"

# Trello API base URL
BASE_URL = "https://api.trello.com/1"

# Proxy settings (update with your corporate proxy if applicable)
PROXIES = {
    "http": "",
    "https": ""
}

# SSL verification (set to False only for testing, revert to True for production)
VERIFY_SSL = True

# Updated trello_board.json content
BOARD_CONFIG = {
    "name": "Knowledge-Gathering Tool",
    "lists": [
        {
            "name": "To Do",
            "cards": [
                {"title": "Approve requirements.md", "due": "2025-04-20"},
                {"title": "Set up GitHub repository", "due": "2025-04-22"},
                {"title": "Install Python and Node.js", "due": "2025-04-22"},
                {"title": "Provide sample job roles", "due": "2025-04-24"},
                {"title": "Confirm test country for Manage a PPA", "due": "2025-04-24"},
                {"title": "Schedule weekly check-in", "due": "2025-04-21"},
                {"title": "Test existing app.py", "due": "2025-04-26"}
            ]
        },
        {
            "name": "In Progress",
            "cards": [
                {"title": "Develop prototype backend", "due": "2025-05-01"}
            ]
        },
        {
            "name": "Done",
            "cards": []
        }
    ]
}

def create_board(name):
    url = f"{BASE_URL}/boards/"
    query = {
        "name": name,
        "key": API_KEY,
        "token": API_TOKEN
    }
    response = requests.post(url, params=query, proxies=PROXIES, verify=VERIFY_SSL)
    if response.status_code == 200:
        return response.json()["id"], response.json()["url"]
    else:
        raise Exception(f"Failed to create board: {response.text}")

def create_list(board_id, name):
    url = f"{BASE_URL}/lists"
    query = {
        "name": name,
        "idBoard": board_id,
        "key": API_KEY,
        "token": API_TOKEN
    }
    response = requests.post(url, params=query, proxies=PROXIES, verify=VERIFY_SSL)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        raise Exception(f"Failed to create list: {response.text}")

def create_card(list_id, title, due_date):
    url = f"{BASE_URL}/cards"
    query = {
        "name": title,
        "idList": list_id,
        "key": API_KEY,
        "token": API_TOKEN
    }
    if due_date:
        due = datetime.strptime(due_date, "%Y-%m-%d").isoformat()
        query["due"] = due
    response = requests.post(url, params=query, proxies=PROXIES, verify=VERIFY_SSL)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        raise Exception(f"Failed to create card: {response.text}")

def main():
    try:
        board_name = BOARD_CONFIG["name"]
        print(f"Creating board: {board_name}")
        board_id, board_url = create_board(board_name