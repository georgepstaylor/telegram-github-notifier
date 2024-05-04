import os

class Env:
    try:
        TELEGRAM_BOT_TOKEN=os.environ.get("INPUT_TELEGRAM_BOT_TOKEN")
    except:
        raise Exception("TELEGRAM_BOT_TOKEN not found in environment variables")
    try:
        TELEGRAM_CHAT_ID=os.environ.get("INPUT_TELEGRAM_CHAT_ID")
    except:
        raise Exception("TELEGRAM_CHAT_ID not found in environment variables")

    GH_REPO=os.environ.get("GITHUB_REPOSITORY")
    GH_EVENT = os.environ.get("INPUT_GH_EVENT")
    GH_SHA=os.environ.get("GITHUB_SHA")
    GH_ACTOR=os.environ.get("GITHUB_ACTOR")
    GH_EVENT_NAME=os.environ.get("GITHUB_EVENT_NAME")
    GH_WORKFLOW=os.environ.get("GITHUB_WORKFLOW")