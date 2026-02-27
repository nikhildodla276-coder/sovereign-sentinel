# 🛡️ Sovereign Sentinel
**An enterprise-grade Python monitoring engine for high-availability alerting.**

## 📊 Technical Validation
- **Pylint Score:** 9.39/10 (Aiming for 10.00/10)
- **Style Guide:** Strictly PEP 8 compliant
- **Architecture:** Decoupled logic with environment-based security

## 🛠 Features & Logical Enhancements
Following a rigorous logical audit, the following engineering patterns were implemented:

- **Defensive Networking:** Integrated `timeout` parameters for all HTTP requests to prevent process hanging.
- **Specific Exception Handling:** Replaced generic error catches with targeted `requests.exceptions.RequestException` for better failure diagnosis.
- **Secure Configuration:** Leveraged `python-dotenv` to isolate sensitive API tokens from the source code.
- **Dynamic Payload System:** Refactored notification logic to use a unified argument system (Resolving W0613).

## 🚀 Deployment
1. Clone the repository.
2. Configure `.env` with `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID`.
3. Run `pylint sentinel.py` to verify current health status.
4. Execute `python sentinel.py`.

---
*"Work performed with discipline and according to standards is the highest form of action." — Inspired by Bhagavad Gita 18.23*
