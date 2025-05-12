# utils.py
import os
import requests
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

def send_telegram_message(message: str):
    # .env faylidan bot token va chat ID ni olish
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Xatolik yuzaga kelsa, bu usul xatolikni ko‘rsatadi
    except requests.exceptions.RequestException as e:
        print("Telegramga yuborishda xatolik:", e)
