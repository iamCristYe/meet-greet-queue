import os
import time
import requests
import shutil
import subprocess
import json
import pytz
from datetime import datetime, timedelta
from telegram import Bot


# 获取JSON数据并处理
def fetch_json_data(url):
    import requests

    # 查看当前 requests 使用的代理配置
    proxies = requests.utils.get_environ_proxies("https://example.com")
    print(proxies)
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"fetch data from {url}")
        return response.json()
    else:
        print(f"Failed to fetch data from {url}")
        return None


# 转换并提取数据
def process_event_data(json_data):
    tokyo_tz = pytz.timezone("Asia/Tokyo")
    today = datetime.now(tokyo_tz).strftime(
        "%Y-%m-%d"
    )  # 获取今天的东京时间，格式为YYYY-MM-DD

    # 获取appGetEventResponse中的artistArray
    event_response = json_data.get("appGetEventResponse", {})
    artist_array = event_response.get("artistArray", [])

    result_tz_ids = []  # 用于存储匹配到的tzId

    # 遍历artistArray，查找artName中包含"坂"的字典
    for artist in artist_array:
        # print(artist["artName"])
        art_name = artist.get("artName", "")
        if "坂" in art_name:  # 如果artName中包含"坂"
            event_array = artist.get("eventArray", [])
            # 查找eventArray中dateDate为今天的事件
            for event in event_array:
                for date in event["dateArray"]:
                    event_date = date.get("dateDate", "")
                    if event_date == today:  # or True:
                        # for item in date["timeZoneArray"]: # Fisrt tzId is OK
                        tz_id = date["timeZoneArray"][0].get("tzId", "")
                        result_tz_ids.append(
                            {
                                "tzId": "e" + str(tz_id),
                                "name": event["evtName"],
                                "date": event_date,
                            }
                        )
    print(result_tz_ids)
    return result_tz_ids


def get_tzId():
    url = "https://api.fortunemusic.app/v1/appGetEventData/"

    # 获取JSON数据
    json_data = fetch_json_data(url)
    with open("event_today.json", "w") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    if json_data:
        # 处理数据并获取符合条件的tzId
        tz_ids = process_event_data(json_data)

        # 打印结果
        if tz_ids:
            print("Today's event tzIds:", tz_ids)
            return tz_ids
        else:
            print("No events found for today with '坂'.")
    else:
        print("No data fetched.")


# 下载并处理文件
def download_and_process(tzId):
    try:
        # 定义curl命令
        curl_command = [
            "curl",
            "-d",
            '{"eventId":"' + tzId + '"}',
            "-H",
            "Content-Type: application/json",
            "-X",
            "POST",
            "https://meets.fortunemusic.app/lapi/v5/app/dateTimezoneMessages",
        ]

        # 获取当前时间戳
        tokyo_tz = pytz.timezone("Asia/Tokyo")
        timestamp = datetime.now(tokyo_tz).strftime("%m%d-%H%M%S")

        # 定义输出文件名
        output_file = f"{tzId}_{timestamp}.json"

        # 执行curl命令并将结果保存到文件
        with open(output_file, "w") as file:
            result = subprocess.run(curl_command, stdout=file)
    except:
        pass


# 创建7z压缩文件
def create_7z_archive():
    tokyo_tz = pytz.timezone("Asia/Tokyo")
    timestamp = datetime.now(tokyo_tz).strftime("%Y%m%d")
    archive_path = os.path.join(".", timestamp + ".7z")
    subprocess.run(["7z", "a", archive_path, "*.json"], check=True)  # 调用7z命令
    # return archive_path


# 发送压缩文件到Telegram
async def send_to_telegram(token, chat_id):
    bot = Bot(token=token)
    tokyo_tz = pytz.timezone("Asia/Tokyo")
    timestamp = datetime.now(tokyo_tz).strftime("%Y%m%d")
    archive_path = os.path.join(".", timestamp + ".7z")
    await bot.send_document(chat_id=chat_id, document=open(archive_path, "rb"))


async def main():
    # 配置参数
    # download_url_list = [
    #     "https://example.com/file1",
    #     "https://example.com/file2",
    # ]  # 替换为你的下载URL列表
    # output_dir = "./downloads"  # 文件下载的保存目录
    duration_s = 2 * 3600  # 设定下载时间为2小时
    telegram_token = os.environ["bot_token"]  # 替换为你的Telegram bot token
    telegram_chat_id = os.environ["chat_id"]  # 替换为你的频道或群组ID
    await send_to_telegram(telegram_token, telegram_chat_id)

    # return     创建下载目录（如果不存在）

    tzId_list = []
    for item in get_tzId():
        tzId_list.append(item["tzId"])

    end_time = datetime.now() + timedelta(seconds=duration_s)

    # 下载并处理文件
    while datetime.now() < end_time:
        for tzId in tzId_list:
            download_and_process(tzId)
        time.sleep(20)  # 每20s下载一次

    # 创建7z压缩文件
    create_7z_archive()

    # 发送到Telegram频道
    send_to_telegram(telegram_token, telegram_chat_id)


import asyncio

if __name__ == "__main__":
    asyncio.run(main())
