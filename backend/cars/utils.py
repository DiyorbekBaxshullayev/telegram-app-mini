# utils.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_telegram_message(message: str):
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')

    if not BOT_TOKEN or not CHAT_ID:
        print("Bot token yoki chat ID topilmadi!")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Xatolik yuzaga kelsa, bu usul xatolikni ko‘rsatadi
        if response.status_code == 200:
            print("Xabar muvaffaqiyatli yuborildi.")
        else:
            print(f"Telegramga yuborishda muammo yuz berdi: {response.text}")
    except requests.exceptions.RequestException as e:
        print("Telegramga yuborishda xatolik:", e)
