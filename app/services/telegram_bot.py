import os
import requests
from dotenv import load_dotenv

load_dotenv()


class TelegramBot:

    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")

    def send_message(self, message: str):

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        payload = {
            "chat_id": self.chat_id,
            "text": message
        }

        try:
            res = requests.post(url, data=payload)
            print("STATUS:", res.status_code)
            print("RESPONSE:", res.text)

        except Exception as e:
            print("ERROR:", e)