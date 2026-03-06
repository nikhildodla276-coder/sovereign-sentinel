"""o
Sentinel System: A robust job monitoring and alerting tool.
This module scrapes target URLs for keywords and sends via Telegram.
"""

# Group 1: Standard Libraries (Built into Python)
from datetime import datetime
import os
import time

# Group 2: Third-Party Libraries (Installed via pip)
import requests
import urllib3
from dotenv import load_dotenv

# load secrets from .env file
load_dotenv()
urllib3.disable_warnings()

# Your Telegram credentials loaded from hidden file
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Pretend to be a real browser
HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/91.0.4472.124 Safari/537.36'
    )
}

# The real internship website to monitor
TARGET_URL = "https://internshala.com/internships/artificial-intelligence-internship"
KEYWORD = "artificial intelligence"


# This function is defined ONCE before the loop
def send_telegram_message(message):
    """Sends a notification string to the Telegram bot via the API."""
    api_url = f"https://api.telegram.org/bot{Token}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': "HTML"

    }
    res = request.post(api_url, data=payload, timeout=10)
    print(f"Server Response: {res.status_code} - {res.text}")
    if res.status_code ==200:
        print("Notification delivered successfully.")
    else:
        print("Handshake failed. Check ID/Token or Bot status.")


# Main loop - runs forever checking the website
while True:
    try:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] Checking target website...")

        response = requests.get(
            TARGET_URL,
            headers=HEADERS,
            verify=False,
            timeout=10
        )

        page_content = response.text.lower()
        print(f"[{current_time}] DEBUG: Received {len(page_content)} characters.")

        if KEYWORD in page_content:
            print(f"[{current_time}] Target Found: Sending Telegram notification....")
            message = f"<b>Sentinel Alert!</b>\nKeyword '<b>{KEYWORD}</b>' found!\nURL: {TARGET_URL}\nTime: {current_time}"
            send_telegram_message(message)
            break


        else:
             print(f"[{current_time}] Keyword not found. Checking again in 60 seconds...")
             time.sleep(60)


    except requests.exception.RequestException as e:
        print(f"Connection/Network Error: {e}")
        time.sleep(10)
