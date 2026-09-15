rom telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    keyboard = [[InlineKeyboardButton("🔗 الانتقال إلى الموقع", url="https://konami-rrgp.onrender.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_message = f"مرحباً بك يا {user_name} في بوت Konami Coins! 🎉\n\nاضغط على الرابط بالأسفل للانتقال إلى الموقع:"
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

def main():
    TOKEN = "8636218822:AAHbloHi09L-Ooh9ezaVGgCDCjoNwH0oMjg"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main() 
