import os
import requests

# جلب التوكن والمعرف من متغيرات البيئة
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# الرسالة التي سيتم إرسالها (يمكنك تعديلها)
message = "🌟 Word of the Day 🌟\n\nResilient (adj.): able to recover quickly from difficulties\n\n🔁 Stay resilient and keep learning!"

# رابط API الخاص بإرسال الرسائل
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# إعداد البيانات المطلوبة
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

# إرسال الرسالة
response = requests.post(url, data=payload)

# طباعة الاستجابة لتسهيل التصحيح
print("Status Code:", response.status_code)
print("Response:", response.text)
