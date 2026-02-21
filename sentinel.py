import requests
import urllib3
import time
from datetime import datetime


urllib3.disable_warnings()

while True:
    response = requests.get("https://www.wikipedia.org", verify=False)
    page_content = response.text.lower()
    current_time = datetime.now().strftime("%H:%M:%S")


    if "wikipedia" in page_content:
        print(f"[{current_time}] Sucess: Target 'wikipedia' is online and active.")

    else:
        print(f"[{current_time}] Warning: Connection active but keyword missing.")

    print("Sentinel standing by... next check in 10 seconds.")
    time.sleep(10)

