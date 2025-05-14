def get_comment(event: dict, *args: str) -> str:
    comment_path: list = []
    for key in args:
        obj = event.get(key)
        comment_path.append(obj)
        event = obj
    comment: str = comment_path[-1]
    return comment if isinstance(comment, str) else ""


def handle_activity(events: list[dict], show_messages: bool = False) -> None:
    if not events:
        print("No recent activity found")
        return
    for event in events:
        repo_name: str = event.get("repo", {}).get("name", "unknown repo")
        match event["type"]:
            case "PushEvent":
                commits_count: int = len(
                    event.get("payload", {}).get("commits", [])
                )
                print(f"- Pushed {commits_count} commits to {repo_name}")
            case "WatchEvent":
                print(f"- Starred {repo_name}")
            case "ForkEvent":
                print(f"- Forked repo from {repo_name}")
            case "PullRequestEvent":
                action: str = (
                    event.get("payload", {}).get("action", "").capitalize()
                )
                print(f"- {action} pull request in {repo_name}")
            case "PullRequestReviewEvent":
                if show_messages is True:
                    review: str = str(
                        get_comment(event, "payload", "review", "body") or ""
                    )
                else:
                    review: str = ""
                print(f"- Reviewed pull request to {repo_name}. Review:")
                print(f"-> {review}")
            case "CommitCommentEvent":
                if show_messages is True:
                    comment: str = str(
                        get_comment(event, "payload", "comment") or ""
                    )
                else:
                    comment: str = ""
                print(f"- Commented commit in {repo_name}. Comment message:")
                print(f"-> {comment}")
            case "IssueCommentEvent":
                if show_messages is True:
                    comment: str = str(
                        get_comment(event, "payload", "issue", "body") or ""
                    )
                else:
                    comment: str = ""
                print(f"- Commented issue in {repo_name}. Comment message")
                print(f"-> {comment}")
            case _:
                print(f"- {event['type']} event in {repo_name} not handled!")
