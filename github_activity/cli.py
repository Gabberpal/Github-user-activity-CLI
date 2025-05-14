import requests
import argparse
from github_activity.utils import handle_activity


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHub recent user activity")
    parser.add_argument("username", help="GitHub username")
    parser.add_argument("--show-messages",
                        action="store_true",
                        help="Show user comments and messages")

    args = parser.parse_args()
    username: str = args.username
    show_messages: bool = args.show_messages

    url: str = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url)

    if response.status_code == 200:
        events: list[dict] = response.json()
        handle_activity(events=events, show_messages=show_messages)
    else:
        print(f"Failed to fetch data for user {username}\n"
              f"Status code: {response.status_code}")
