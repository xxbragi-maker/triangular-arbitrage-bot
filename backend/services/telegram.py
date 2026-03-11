import requests
from backend.config import TELEGRAM_TOKEN, TELEGRAM_CHAT


def notify(message: str):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT:
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    try:
        requests.post(
            url,
            data={
                "chat_id": TELEGRAM_CHAT,
                "text": message
            },
            timeout=10
        )
    except Exception:
        pass
