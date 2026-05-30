# Standard libraries
import os
import time
from datetime import datetime

# Third-party libraries
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Constants
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

SEEN_LOG = "seen_log.txt"

TARGET_URL = "https://internshala.com/internships/artificial-intelligence-internship"


def load_seen():
    """Loads all previosly seen internship URLs from seen_log.txt"""
    if not os.path.exists(SEEN_LOG):
        return set()
    with open(SEEN_LOG, "r", encoding="utf-8") as f:
        lines = f.readlines()
        return set(line.strip() for line in lines)

def save_seen(url):
    """This function takes one url and appends it to seen_log.txt"""
    with open(SEEN_LOG, "a", encoding="utf-8") as f:
        f.write(url + "\n")

def send_telegram_message(text):
    """It sends your formatted message to telegram via their API"""
    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(telegram_url, data=payload, timeout=10)
    print(f"Server Response: {response.status_code}")
    if response.status_code == 200:
        print("Notification delieverd successfully.")
    else:
        print("Handshake failed. Check ID/Token or Bot statues.")

HEADERS = {
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/91.0.4472.124 Safari/537.36"
}

