from env import Env
import requests

telegram_base_url = "https://api.telegram.org/bot"

def telegram_check_token():
    try:
        user = requests.get(telegram_base_url + Env.TELEGRAM_BOT_TOKEN + "/getMe")
        if user.status_code == 200:
            if user.json()["ok"]:
                return True
            else:
                raise Exception("Authentication failed with Telegram API")
        else:
            raise Exception("Request did not return 200 status code")
    except Exception as e:
        raise Exception("Request failed to connect to Telegram API with error: " + str(e))

def telegram_send_message(message, inline_keyboard=[]):
    response = requests.post(
        telegram_base_url + Env.TELEGRAM_BOT_TOKEN + "/sendMessage",
        json={
            "chat_id": Env.TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown",
            "reply_markup": {
                "inline_keyboard": inline_keyboard
            }
        }
    )
    print(response.json())

def build_github_event_link():
    github_base_url = f"https://github.com/{Env.GH_REPO}"

    event_name_url_map = {
        "issue_comment": "issues",
        "issues": "issues",
        "pull_request": "pull",
        "pull_request_review": "pull",
        "pull_request_review_comment": "pull",
        "push": "commit"
    }

    if Env.GH_EVENT_NAME in ["pull_request_review_comment", "pull_request"]:
        return f"{github_base_url}/{event_name_url_map[Env.GH_EVENT_NAME]}/{Env.GH_EVENT['number']}"
    elif Env.GH_EVENT_NAME in ["issue_comment", "issues"]:
        return f"{github_base_url}/{event_name_url_map[Env.GH_EVENT_NAME]}/{Env.GH_EVENT['issue']['number']}"
    elif Env.GH_EVENT_NAME == "push":
        return f"{github_base_url}/{event_name_url_map[Env.GH_EVENT_NAME]}/{Env.GH_SHA}"
    else:
        return f"{github_base_url}/{event_name_url_map[Env.GH_EVENT_NAME]}"

def build_github_user_link(username):
    return f"https://github.com/{username}"

def build_message(event_name):
    event_link = build_github_event_link()
    if event_name in ["issues", "issue_comment"]:
        return (f"*Event:* [{event_name}]({event_link}) by [{Env.GH_ACTOR}](https://github.com/{Env.GH_ACTOR})\n"
               f"*Action:* {event_name}\n"
               f"*Repo:* [{Env.GH_REPO}](https://github.com/{Env.GH_REPO})")
    elif event_name == "pull_request":
        return (f"*Event:* [{event_name}]({event_link}) by [{Env.GH_ACTOR}](https://github.com/{Env.GH_ACTOR})\n"
                f"*Action:* {Env.GH_EVENT['action']}\n"
                f"*Repo:* [{Env.GH_REPO}](https://github.com/{Env.GH_REPO})")
    else:
        return (f"*Event:* [{event_name}]({event_link}) by [{Env.GH_ACTOR}](https://github.com/{Env.GH_ACTOR})\n"
                f"*Repo:* [{Env.GH_REPO}](https://github.com/{Env.GH_REPO})")
def main():
    if telegram_check_token():
        print("Token is valid")
        event_link = build_github_event_link()
        telegram_send_message(
            message=build_message(Env.GH_EVENT_NAME),
            inline_keyboard=[
                [
                    {"text": "Event", "url": event_link},
                    {"text": "User", "url": build_github_user_link(Env.GH_ACTOR)},
                    {"text": "Repo", "url": f"https://github.com/{Env.GH_REPO}"}
                ]
            ]
        )
    else:
        exit(1)


if __name__ == "__main__":
    main()