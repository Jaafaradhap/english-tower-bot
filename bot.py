
import requests
from datetime import datetime

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

def daily_lesson():
    now = datetime.now().strftime("%Y-%m-%d")
    text = f"📘 *English Tower Daily Lesson - {now}*\n\n"
    text += "🔤 *Word of the Day*: inspiration\n"
    text += "🗣️ *Phrase*: Follow your dreams.\n"
    text += "❓ *Question*: What motivates you to learn English?\n"
    text += "📖 *Short Text*:\nNever stop learning. Every day brings a new chance to improve."
    send_message(text)

if __name__ == "__main__":
    daily_lesson()
