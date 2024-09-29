import pytz
from datetime import datetime


tokyo_tz = pytz.timezone("Asia/Tokyo")
today = datetime.now(tokyo_tz).hour
print(today)