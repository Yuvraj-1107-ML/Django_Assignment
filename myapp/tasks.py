from celery import shared_task
from celery import shared_task
from django.core.mail import send_mail as django_send_mail
from django.conf import settings


@shared_task
def send_mail(user_email, username):

    subject = 'Welcome to My Assignment!'
    message = (
        f"Hi {username},\n\n"
        "Thank you for registering.\n\n"
        "In this Assignment, you interact with Telegram bot :\n"
        "Go to this Bot to test  https://t.me/DJango_Testing_bot\n\n"
        "Best regards,\n"
        "Yuvraj Dawnde \n"
        "Contact: +919343299593"
    )
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    django_send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )
