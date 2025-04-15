from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🚗 Mashinalar", web_app=WebAppInfo(url="https://telegram-app-mini.vercel.app/"))]
    ]
    await update.message.reply_text("RentCar'ga xush kelibsiz!", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

app = Application.builder().token("").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
