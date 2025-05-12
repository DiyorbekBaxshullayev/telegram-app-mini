# cars/utils.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()  # .env faylni yuklaydi

def send_telegram_message(message: str):
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')

    if not BOT_TOKEN or not CHAT_ID:
        print("❌ BOT_TOKEN yoki CHAT_ID topilmadi.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("✅ Xabar muvaffaqiyatli yuborildi.")
    except requests.exceptions.RequestException as e:
        print("❌ Telegramga yuborishda xatolik:", e)
