import subprocess
import time
from datetime import datetime

def save_curl_result():
    # 定义curl命令
    curl_command = [
        'curl', 
        '-d', '{"eventId":"e24082"}', 
        '-H', 'Content-Type: application/json', 
        '-X', 'POST', 'https://meets.fortunemusic.app/lapi/v5/app/dateTimezoneMessages'
    ]
    
    # 获取当前时间戳
    timestamp = datetime.now().strftime('%m%d-%H%M%S')
    
    # 定义输出文件名
    output_file = f'{timestamp}.json'
    
    # 执行curl命令并将结果保存到文件
    with open(output_file, 'w') as file:
        result = subprocess.run(curl_command, stdout=file)
    
    if result.returncode == 0:
        print(f"Successfully saved curl result to {output_file}")
    else:
        print(f"Failed to execute curl command, return code: {result.returncode}")

print("Script started. Press Ctrl+C to exit.")
try:
    while True:
        save_curl_result()
        time.sleep(10)  # 等待10秒
except KeyboardInterrupt:
    print("Script stopped.")