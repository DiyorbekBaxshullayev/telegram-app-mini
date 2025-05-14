from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚘 Ijaraga olish", web_app=WebAppInfo(url="https://rentcar-front.vercel.app/"))],
        [InlineKeyboardButton("📍 Manzilni ko‘rish", web_app=WebAppInfo(url="https://rentcar-map.vercel.app/"))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Ijaraga olish yoki manzilimizni ko‘rish uchun tugmani bosing 👇", reply_markup=reply_markup)

# Botni ishga tushirish
app = ApplicationBuilder().token("").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
