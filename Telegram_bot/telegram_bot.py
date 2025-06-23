import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')
django.setup()

from django.contrib.auth.models import User
from myapp.models import TelegramUser
from decouple import config

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes



API_KEY = config('TELEGRAM_BOT_TOKEN')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    chat_id = update.effective_chat.id


    user = User.objects.first()
    if user:
        TelegramUser.objects.update_or_create (
            user=user,
            defaults={'telegram_username': username}
        )
        reply = f"Thanks @{username}! Your Telegram username has been saved."
    else:
        reply = " No Django user found to link."

    await context.bot.send_message(chat_id=chat_id, text=reply)


def main():
    
    app = ApplicationBuilder().token(API_KEY).build()

   
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Telegram bot is running")
    
    app.run_polling()

if __name__ == '__main__':
             main()
