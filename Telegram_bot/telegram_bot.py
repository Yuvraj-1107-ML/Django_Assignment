import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')  
django.setup()

import requests
from django.contrib.auth.models import User
from myapp.models import TelegramUser
from decouple import config


BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

#  Function to handle a single update message
def handle_update(update):
    message = update.get('message', {})
    chat_id = message['chat']['id']
    username = message['from'].get('username', '')

    # Link to the first user (for demo)
    user = User.objects.first()
    if user:
        TelegramUser.objects.update_or_create(
            user=user,
            defaults={'telegram_username': username}
        )
        reply = f"Thanks @{username}! Your Telegram username has been saved."
    else:
        reply = " No Django user found to link this Telegram username."

    requests.post(URL + "sendMessage", data={
        "chat_id": chat_id,
        "text": reply
    })

#  simple polling loop to test
def run_bot():
    offset = None
    print("Bot is running... Press CTRL+C to stop.")

    while True:
        updates = requests.get(URL + "getUpdates", params={"timeout": 100, "offset": offset}).json()
        for update in updates.get("result", []):
            handle_update(update)
            offset = update["update_id"] + 1


if __name__ == '__main__':
    run_bot()
