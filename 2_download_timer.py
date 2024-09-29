import subprocess
import time
from datetime import datetime


def save_curl_result(tzId):
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
    timestamp = datetime.now().strftime("%m%d-%H%M%S")

    # 定义输出文件名
    output_file = f"{tzId}_{timestamp}.json"

    # 执行curl命令并将结果保存到文件
    with open(output_file, "w") as file:
        result = subprocess.run(curl_command, stdout=file)

    if result.returncode == 0:
        print(f"Successfully saved curl result to {output_file}")
    else:
        print(f"Failed to execute curl command, return code: {result.returncode}")


print("Script started. Press Ctrl+C to exit.")
try:
    while True:

        current_time = datetime.now()
        print(current_time)
        if (
            current_time.hour >= 8 and current_time.hour <= 21
        ):  # current_time.minute >= 30:
            save_curl_result("e24414")

            # time.sleep(10)  # 等待10秒
        time.sleep(20)
except KeyboardInterrupt:
    print("Script stopped.")
