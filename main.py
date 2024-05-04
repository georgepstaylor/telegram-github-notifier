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

def main():
    if telegram_check_token():
        print("Token is valid")
        telegram_send_message(
            message="Hello, World!"
        )
    else:
        exit(1)


if __name__ == "__main__":
    main()