import requests
import json
from utils import handle_activity

username: str = "orbeckst"
url: str = f"https://api.github.com/users/{username}/events/public"

response = requests.get(url)

if response.status_code == 200:
    events: list[dict] = response.json()
    handle_activity(events=events)

with open("response.json", "w") as file:
    json.dump(events, file, indent=4)
