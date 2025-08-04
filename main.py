import os
import json
import random
import logging
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

# إعداد تسجيل الأخطاء
logging.basicConfig(level=logging.INFO)

# جلب التوكن و Chat ID من المتغيرات البيئية
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

# تحميل المحتوى من ملف JSON
with open("content.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def send_daily_message():
    word = random.choice(data["words"])
    sentence = random.choice(data["sentences"])
    rule = random.choice(data["rules"])
    text = random.choice(data["texts"])

    message = f"""📚 *Daily English Dose* 📚

🔤 *Word of the Day:* `{word}`
🗣 *Sentence:* _{sentence}_
📘 *Grammar Tip:* {rule}
📖 *Short Text:* {text}
"""

    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

# جدولة الإرسال اليومي
scheduler = BlockingScheduler()
scheduler.add_job(send_daily_message, 'cron', hour=10)  # وقت الإرسال: 10 صباحًا حسب UTC
scheduler.start()
