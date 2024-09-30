import pytz
from datetime import datetime


tokyo_tz = pytz.timezone("Asia/Tokyo")
today = datetime.now(tokyo_tz).hour
print(today)

tzId_list = []
for item in {}:
    tzId_list.append(item["tzId"])

if len(tzId_list) == 0:
    print(0)
