import requests
import urllib3
import time
from datetime import datetime


urllib3.disable_warnings()

TOKEN = "MY_BOT_TOKEN_HERE"
CHAT_ID = "MY_CHAT_ID_HERE"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

while True:
    try:
        response = requests.get("https://www.wikipedia.org", headers=headers, verify=False)
        page_content = response.text.lower()
        current_time = datetime.now().strftime("%H:%M:%S")

        print(f"[{current_time}] DEBUG: Received {len(page_content)} characters from site.")


        if "wikipedia" in page_content:
            print(f"[{current_time}] Target Found! Attempting to notify Telegram...")


            api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

            payload = {
                'chat_id': CHAT_ID,
                'text': f"Sentinel Alert: Wikipedia is ONLINE at {current_time}"
              }

            res = requests.post(api_url, data=payload)


            print(f"Server Response: {res.status_code} - {res.text}")

            if res.status_code == 200:
                print("Notification delivered successfully.")
                break


        else:
            print("Handshake failed. Check ID/Token or Bot status.")
            break


    except Exception as e:
        print(f"An error occured: {e}")
        time.sleep(10)






