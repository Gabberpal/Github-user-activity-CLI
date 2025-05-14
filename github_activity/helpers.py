def get_comment(event: dict, *args: str, **kwargs) -> str:
    current = event
    for key in args:
        if not isinstance(current, dict):
            return ""
        current = current.get(key)
    return current if isinstance(current, str) else ""


def get_repo_name(event: dict) -> str:
    repo_name: str = event.get("repo", {}).get("name", "unknown repo")
    return repo_name


def print_optional_message(comment: str) -> None:
    print(
        f"-> {comment or 'You can display the message by adding --show-messages'}"
    )
