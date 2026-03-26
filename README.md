# Sovereign Sentinel

A Python automation bot that continuously monitors Internshala for new AI internship listings and delivers instant alerts via Telegram.

---

## What It Does

Sovereign Sentinel runs in the background and checks the Internshala AI internships page every 60 seconds. When a new listing is found that has not been seen before, it immediately sends a Telegram notification with the title and link. Already-seen listings are tracked in a local log file to prevent duplicate alerts.

---

## How It Works

1. Fetches the Internshala AI internships page using a browser-like request header
2. Parses the HTML using BeautifulSoup to extract internship titles and links
3. Compares each listing against `seen_log.txt` to check if it is new
4. Sends a Telegram alert for any new listing found
5. Saves the new listing URL to `seen_log.txt`
6. Waits 60 seconds and repeats
7. On connection failure, waits 10 seconds and retries automatically

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| requests | HTTP requests to Internshala and Telegram API |
| BeautifulSoup4 | HTML parsing |
| python-dotenv | Secure environment variable management |
| Telegram Bot API | Delivering alerts |

---

## Project Structure

```
sovereign-sentinel/
├── sentinel.py        # Main bot logic
├── seen_log.txt       # Tracks already-alerted internship URLs
├── requirements.txt   # Python dependencies
├── .env               # API credentials (not tracked by Git)
├── .gitignore         # Excludes .env and other sensitive files
└── LICENSE
```

---

## Setup and Usage

### 1. Clone the repository

```bash
git clone https://github.com/nikhildodla276-coder/sovereign-sentinel.git
cd sovereign-sentinel
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create your `.env` file

```
TELEGRAM_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

### 4. Run the bot

```bash
python sentinel.py
```

The bot will start monitoring immediately and send Telegram alerts when new AI internships are posted.

---

## Code Quality

- Pylint Score: **10/10**
- PEP 8 compliant
- Environment-based credential management via python-dotenv
- Targeted exception handling for network failures
- Timeout parameter on all HTTP requests to prevent process hanging

---

## License

MIT License
