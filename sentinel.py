"""
Sentinel System: A robust job monitoring and alerting tool.
This module scrapes target URLs for internships title with link and sends via Telegram.
"""

# Standard Libraries
from datetime import datetime
import os
import time

# Third-Party Libraries
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

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
BASE_URL = "https://internshala.com"
SEEN_LOG = "seen_log.txt"


def load_seen():
    """Loads previously seen internship URLs from file."""
    if not os.path.exists(SEEN_LOG):
        return set()
    with open(SEEN_LOG, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f.readlines())


def save_seen(url):
    """Saves a new internship URL to the seen log file."""
    with open(SEEN_LOG, "a", encoding="utf-8") as f:
        f.write(url + "\n")


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
            timeout=10
        )

        soup = BeautifulSoup(page_response.text, "html.parser")
        internships = soup.find_all("div", class_="internship_meta")
        seen = load_seen()

        print(f"[{current_time}] Found {len(internships)} listings.")

        for item in internships:
            title_tag = item.find("h3", class_="job-internship-name")
            if title_tag:
                link = title_tag.find("a")
                if link:
                    href = link["href"]
                    title = title_tag.text.strip()
                    if href not in seen:
                        alert = (
                            f"<b>New Internship Found!</b>\n"
                            f"Title: <b>{title}</b>\n"
                            f"URL: {BASE_URL}{href}\n"
                            f"Time: {current_time}"
                        )
                        send_telegram_message(alert)
                        save_seen(href)
                        seen.add(href)

        print(
            f"[{current_time}] "
            f"Scan complete. Checking again in 60 seconds..."
        )
        time.sleep(60)

    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
        time.sleep(10)
