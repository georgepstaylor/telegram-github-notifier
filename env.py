import os

class Env:
    try:
        TELEGRAM_BOT_TOKEN=os.environ.get("TELEGRAM_BOT_TOKEN")
    except:
        raise Exception("TELEGRAM_BOT_TOKEN not found in environment variables")
    try:
        TELEGRAM_CHAT_ID=os.environ.get("TELEGRAM_CHAT_ID")
    except:
        raise Exception("TELEGRAM_CHAT_ID not found in environment variables")