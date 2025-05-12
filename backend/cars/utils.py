# cars/utils.py
import requests

def send_telegram_message(message: str):
    BOT_TOKEN = '6176561737:AAGCeN60gXcjIjYNImgzzKSfMh6gsZItJMs'
    CHAT_ID = '2007510369'
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Telegramga yuborishda xatolik:", e)
