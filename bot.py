(keyboard)
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
