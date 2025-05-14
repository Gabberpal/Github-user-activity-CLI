from handlers import handlers


def handle_activity(events: list[dict], show_messages: bool = False) -> None:
    if not events:
        print("No recent activity found")
        return
    for event in events:
        handler = handlers.get(event["type"])
        if handler:
            handler(event, show_messages=show_messages)
        else:
            print(f"- {event["type"]} event (not hadled yet!)")
