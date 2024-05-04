import os
import json

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
    try:
        GH_EVENT = json.loads(os.environ.get("INPUT_GH_EVENT"))
    except Exception as e:
        raise Exception("Unable to serialize GH_EVENT, or not found\n" + str(e))
    GH_SHA=os.environ.get("GITHUB_SHA")
    GH_ACTOR=os.environ.get("GITHUB_ACTOR")
    GH_EVENT_NAME=os.environ.get("GITHUB_EVENT_NAME")
    GH_WORKFLOW=os.environ.get("GITHUB_WORKFLOW")