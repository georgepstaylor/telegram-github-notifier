import telegram
from env import Env

def main():
    client = telegram.Bot(token=Env.TELEGRAM_BOT_TOKEN)
    client.send_message(chat_id=Env.TELEGRAM_CHAT_ID, text="Hello, World!")
