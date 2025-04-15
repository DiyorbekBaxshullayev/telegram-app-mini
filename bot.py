from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# start komandasi handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Rent a Car 🚗", web_app=WebAppInfo(url="https://telegram-app-mini.vercel.app/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Ijaraga olish uchun tugmani bosing 👇", reply_markup=reply_markup)

app = ApplicationBuilder().token("").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()