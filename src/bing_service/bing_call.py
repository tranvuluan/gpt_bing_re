import asyncio
import json
from pathlib import Path
from nest_asyncio import apply

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle

bot = None

async def init_chatbot():
    global bot
    cookies = json.loads(open(str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    print('BOT INITITALED')
    return bot

async def call_bing_bot(message: str):
    global bot
    if bot is None:
        # Initialize the bot if it hasn't been initialized yet
        print('BOT IS NONE')
        bot = init_chatbot()
    else:
        print('BOT HAS BEEN INITIALED')

    try:
        response = await bot.ask_stream(
            prompt=message,
            conversation_style=ConversationStyle.balanced,
            simplify_response=True,
        )
        # If you are using non-ascii characters, you need to set ensure_ascii=False
        # print(json.dumps(response, indent=2, ensure_ascii=False))
        # Raw response
        print(response)
        # print(response)
        assert response
        return response
    except Exception as error:
        raise error

# Manually initialize the chatbot before running the test_ask function
