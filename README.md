#  Django Assignment — JWT Authentication, Celery with redis  & Telegram Bot

This project demonstrates:
- ✅ User registration with JWT authentication
- ✅ Public and protected API endpoints
- ✅ Celery background tasks for sending a welcome email
- ✅ A Telegram bot that stores Telegram usernames in the database

---

## ⚙️ **Setup Instructions**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Yuvraj-1107-ML/Django_Assignment.git
cd Django_Assignment

```

### 2️⃣ Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3️⃣ Install required packages

```bash

pip install -r requirements.txt

```
### 4️⃣ Create \`.env\` file

Create a `.env` file in your project root with the following variables:

```env
# Email configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

# Telegram Bot Token
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN

# Celery broker URL (using Redis)
CELERY_BROKER_URL=redis://localhost:6379/0

```



### 5️⃣ Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate

```

### 6️⃣ Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser

```

##  **How to Run the Project**

### ✅ 1. Start Redis (for Celery)

Make sure Redis is running.

Example for Windows:
```bash
redis-server
```


### ✅ 2. Start the Django server

```bash
python manage.py runserver


```

### ✅ 3. Start the Celery worker

In a **new terminal**, with the virtual environment activated:
```bash
celery -A Core worker --loglevel=info
```


### ✅ 4. Run the Telegram bot

In a **new terminal**, with the virtual environment activated:

```bash
python telegram_bot.py
```



## 🔑 **Environment Variables**

This project uses the following **environment variables** (configured in `.env`):

| Variable | Purpose |
| -------- | ------- |
| EMAIL_HOST | SMTP server for sending emails |
| EMAIL_PORT | SMTP port |
| EMAIL_USE_TLS | Use TLS for secure email |
| EMAIL_HOST_USER | Your email address |
| EMAIL_HOST_PASSWORD | App-specific email password |
| TELEGRAM_BOT_TOKEN | Telegram bot token |
| CELERY_BROKER_URL | Broker URL for Celery (Redis recommended) |

👉 **.env copy paste to test the project:** [Environment Variables](https://docs.google.com/document/d/1--KYI_QfU7tbjfYG_xw0jcevI3qmNcSXuoTDRB5KipM/edit?tab=t.rttrnlcyq04c)

---

##  **API Documentation**

👉 **Full API Documentation:** [Google Docs — API Documentation](https://docs.google.com/document/d/1--KYI_QfU7tbjfYG_xw0jcevI3qmNcSXuoTDRB5KipM/edit?usp=sharing)

---

## 📬 **How the Telegram Bot Works**

- The Telegram bot runs as a separate Python script (`telegram_bot/telegram_bot.py`).
- It polls Telegram for incoming messages.
- When a user sends a message, their Telegram username is stored in the database linked to a Django user.
- You can check saved usernames via the `/api/telegram-users/` endpoint (JWT required).

👉 **Try it live:** [DJango_Testing_bot](https://t.me/DJango_Testing_bot)

---

## ✅ **How to Test the Full Flow**

1️⃣ Register a user via `/api/register/`  
2️⃣ Login via `/api/login/` → copy the \`access\` token  
3️⃣ Call `/api/users/` with the \`Authorization\` header  
4️⃣ Send a message to [DJango_Testing_bot](https://t.me/DJango_Testing_bot)  
5️⃣ Call `/api/telegram-users/` with your \`access\` token to see your Telegram username saved!

---

## ✅ **All done — Looking forward to you Message**



