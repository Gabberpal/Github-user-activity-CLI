import requests
import json


username: str = "orbeckst"
url: str = f"https://api.github.com/users/{username}/events/public"


def handle_activity(events: list[dict],
                    show_messages: bool = False) -> None:
    if not events:
        print("No recent activity found")
    for event in events:
        repo_name: str = event.get("repo", {}).get("name", "unknown repo")
        match event["type"]:
            case "PushEvent":
                commits_count: int = len(event.get("payload", {}).get("commits", []))
                print(f"- Pushed {commits_count} commits to {repo_name}")
            case "WatchEvent":
                print(f"- Starred {repo_name}")
            case "ForkEvent":
                print(f"- Forked repo from {repo_name}")
            case "PullRequestEvent":
                action: str = event.get("payload", {}).get("action", "").capitalize()
                print(f"- {action} pull request in {repo_name}")
            case "PullRequestReviewEvent":
                if show_messages is True:
                    review: str = event.get("payload", {}).get("review", "").get("body", "")
                    review: str = f"Review: " f"'{review}'"
                else:
                    review: str = ""
                print(f"- Reviewed pull request to {repo_name}", review)
            case "CommitCommentEvent":
                if show_messages is True:
                    comment: str = event.get("payload", {}).get("comment", "")
                    comment: str = f": '{comment}'"
                else:
                    comment: str = ""
                print(f"- Commented commit in {repo_name}", comment)
            case "IssueCommentEvent":
                if show_messages is True:
                    comment: str = event.get("payload", {}).get("issue", {}).get("body", "")
                    comment: str = f", comment: '{comment}'"
                else:
                    comment: str = ""
                print(f"- Commented issue in {repo_name}", comment)


response = requests.get(url)

if response.status_code == 200:
    events: list[dict] = response.json()
    handle_activity(events=events)

with open("response.json", "w") as file:
    json.dump(events, file, indent=4)
