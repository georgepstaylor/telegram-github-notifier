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

def telegram_send_message(message):
    requests.post(
        telegram_base_url + Env.TELEGRAM_BOT_TOKEN + "/sendMessage",
        json={
            "chat_id": Env.TELEGRAM_CHAT_ID,
            "text": message
        }
    )

def build_github_link():
    github_base_url = f"https://github.com/{Env.GH_REPO}"

    event_name_url_map = {
        "issue_comment": "issues",
        "issues": "issues",
        "pull_request": "pulls",
        "pull_request_review_comment": "pulls",
        "push": "commits"
    }

    if Env.GH_EVENT_NAME in ["pull_request_review_comment", "pull_request"]:
        return f"{github_base_url}/{event_name_url_map[Env.GH_EVENT_NAME]}/{Env.GH_EVENT['number']}"
    elif Env.GH_EVENT_NAME in ["issue_comment", "issues"]:
        return f"{github_base_url}/{event_name_url_map[Env.GH_EVENT_NAME]}/{Env.GH_EVENT['issue']['number']}"
    elif Env.GH_EVENT_NAME == "push":
        return f"{github_base_url}/{event_name_url_map[Env.GH_EVENT_NAME]}/{Env.GH_SHA}"
    else:
        return f"{github_base_url}/{event_name_url_map[Env.GH_EVENT_NAME]}"

def main():
    if telegram_check_token():
        print("Token is valid")
        link = build_github_link()
        telegram_send_message(
            message=f"""ACTION: {Env.GH_EVENT_NAME}
                    REPO: {Env.GH_REPO}
                    ACTOR: {Env.GH_ACTOR}
                    LINK: {link}
                    """
        )
    else:
        exit(1)


if __name__ == "__main__":
    main()