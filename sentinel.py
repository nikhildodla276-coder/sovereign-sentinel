"""
Sentinel System: A robust job monitoring and alerting tool.
This module scrapes target URLs for keywords and sends via Telegram.
"""

# Standard Libraries
from datetime import datetime
import os
import time

# Third-Party Libraries
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/91.0.4472.124 Safari/537.36'
    )
}

TARGET_URL = (
    "https://internshala.com"
    "/internships/artificial-intelligence-internship"
)
KEYWORD = "artificial intelligence"


def send_telegram_message(text):
    """Sends a notification string to the Telegram bot via the API."""
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': "HTML"
    }
    response = requests.post(api_url, data=payload, timeout=10)
    print(f"Server Response: {response.status_code}")
    if response.status_code == 200:
        print("Notification delivered successfully.")
    else:
        print("Handshake failed. Check ID/Token or Bot status.")


while True:
    try:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] Checking target website...")

        page_response = requests.get(
            TARGET_URL,
            headers=HEADERS,
            verify=False,
            timeout=10
        )

        page_content = page_response.text.lower()
        print(
            f"[{current_time}] DEBUG: "
            f"Received {len(page_content)} characters."
        )

        if KEYWORD in page_content:
            print(f"[{current_time}] Target Found! Sending alert...")
            alert = (
                f"<b>Sentinel Alert!</b>\n"
                f"Keyword: <b>{KEYWORD}</b> found!\n"
                f"URL: {TARGET_URL}\n"
                f"Time: {current_time}"
            )
            send_telegram_message(alert)
            break

        print(
            f"[{current_time}] "
            f"Keyword not found. Checking again in 60 seconds..."
        )
        time.sleep(60)

    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
        time.sleep(10)
