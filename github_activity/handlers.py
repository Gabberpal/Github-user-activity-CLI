from helpers import get_comment, get_repo_name, print_optional_message


def handle_watch(event: dict, *args, **kwargs) -> None:
    repo_name: str = get_repo_name(event)
    print(f"- Starred {repo_name}")


def handle_push(event: dict, *args, **kwargs) -> None:
    repo_name: str = get_repo_name(event)
    commits_count: int = len(event.get("payload", {}).get("commits", []))
    print(f"- Pushed {commits_count} commits to {repo_name}")


def handle_fork(event: dict, *args, **kwargs) -> None:
    repo_name: str = get_repo_name(event)
    print(f"- Forked repo from {repo_name}")


def handle_pull(event: dict, *args, **kwargs) -> None:
    repo_name: str = get_repo_name(event)
    action: str = event.get("payload", {}).get("action", "").capitalize()
    print(f"- {action} pull request in {repo_name}")


def handle_pull_review(event: dict, *args, **kwargs) -> None:
    repo_name: str = get_repo_name(event)
    if kwargs.get("show_messages") is True:
        review: str = str(get_comment(event, "payload", "review", "body") or "")
    else:
        review: str = ""
    print(f"- Reviewed pull request to {repo_name}. Review:")
    print_optional_message(review)


def handle_commit_comment(event: dict, *args, **kwargs) -> None:
    repo_name: str = get_repo_name(event)
    if kwargs.get("show_messages") is True:
        comment: str = str(get_comment(event, "payload", "comment", "body") or "")
    else:
        comment: str = ""
    print(f"- Commented commit in {repo_name}. Comment message:")
    print_optional_message(comment)


def handle_issue_comment(event: dict, *args, **kwargs) -> None:
    repo_name: str = get_repo_name(event)
    if kwargs.get("show_messages") is True:
        comment: str = str(get_comment(event, "payload", "issue", "body") or "")
    else:
        comment: str = ""
    print(f"- Commented issue in {repo_name}. Comment message")
    print_optional_message(comment)


handlers = {
    "WatchEvent": handle_watch,
    "PushEvent": handle_push,
    "ForkEvent": handle_fork,
    "PullRequestEvent": handle_pull,
    "PullRequestReviewEvent": handle_pull_review,
    "CommitCommentEvent": handle_commit_comment,
    "IssueCommentEvent": handle_issue_comment,
}
