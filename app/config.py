import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Application settings
APP_ENV = os.getenv("APP_ENV", "development")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "data/flights.db"
)

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
NOTIFICATION_EMAIL = os.getenv("NOTIFICATION_EMAIL")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")