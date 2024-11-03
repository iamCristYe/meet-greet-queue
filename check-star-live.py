import requests
from bs4 import BeautifulSoup
import time
from telegram import Bot
import asyncio
import datetime
import os

# Telegram bot token 和频道 ID
TELEGRAM_BOT_TOKEN = os.environ["bot_token"]
TELEGRAM_CHANNEL_ID = os.environ["chat_id"]

# 需要检测的内容
TARGET_MESSAGE = "本日11月3日(日)横浜アリーナにて開催される「超・乃木坂スター誕生！LIVE」昼公演について、奥田いろはが体調不良により、休演致します。"

# 创建 Telegram Bot 实例
bot = Bot(token=TELEGRAM_BOT_TOKEN)


async def check_website():
    url = "https://nogistarlive.jp"

    while True:
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        # print(response.text)
        soup = BeautifulSoup(response.text, "html.parser")

        # 检查是否存在目标消息
        if TARGET_MESSAGE not in soup.get_text():

            # 如果没有找到，发送消息到 Telegram
            await bot.send_message(
                chat_id=TELEGRAM_CHANNEL_ID,
                text="Page updated: https://nogistarlive.jp",
            )
            return

        # 等待 60 秒再检查一次
        print(datetime.datetime.now())
        time.sleep(30)


if __name__ == "__main__":
    asyncio.run(check_website())
