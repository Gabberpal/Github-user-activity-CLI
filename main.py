import requests


username = "Gabberpal"
url = f"https://api.github.com/users/{username}/events/public"


def handle_activity(events):
    if not events:
        print("No recent activity found")
    for event in events:
        repo_name = event.get("repo", {}).get("name", "unknown repo")
        match event["type"]:
            case "PushEvent":
                commits_count = len(event.get("payload", {}).get("commits", []))
                print(f"- Pushed {commits_count} commits to {repo_name}")
            case "WatchEvent":
                print(f"- Starred {repo_name}")
            case "ForkEvent":
                print(f"- Forked repo from {repo_name}")
            case "PullRequestEvent":
                action = event.get("payload", {}).get("action", "").capitalize()
                print(f"- {action} pull request to {repo_name}")


response = requests.get(url)

if response.status_code == 200:
    events = response.json()
    handle_activity(events=events)
