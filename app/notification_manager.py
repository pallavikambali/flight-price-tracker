import smtplib
from email.message import EmailMessage
import requests
from app.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from app.logger import logger

from app.config import (
    SMTP_HOST,
    SMTP_PORT,
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    NOTIFICATION_EMAIL
)


def send_notification(flight, target_price):

    message = EmailMessage()

    message["Subject"] = "Flight Price Alert!"
    message["From"] = EMAIL_ADDRESS
    message["To"] = NOTIFICATION_EMAIL

    message.set_content(f"""
Great news! A flight is within your budget.

Airline: {flight['airline']}
Flight: {flight['flight_number']}
Route: {flight['origin']} to {flight['destination']}

Current Price: ₹{flight['price']}
Your Target: ₹{target_price}
""")

    logger.info("Sending email notification")

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)

        logger.info("Email notification sent successfully")
        print("Email notification sent!")
        return True

    except Exception as error:
        logger.error(
            "Email notification failed: %s",
            type(error).__name__
        )
        print(f"Email notification failed: {type(error).__name__}")
        return False
def send_telegram_notification(flight, target_price):

    message = (
        f"✈️ FlyGo Flight Alert!\n\n"
        f"Airline: {flight['airline']}\n"
        f"Flight: {flight['flight_number']}\n"
        f"Route: {flight['origin']} → {flight['destination']}\n"
        f"Price: ₹{flight['price']}\n"
        f"Target: ₹{target_price}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    try:
        response = requests.post(
            url,
            json={"chat_id": TELEGRAM_CHAT_ID, "text": message},
            timeout=10
        )
        response.raise_for_status()

        if response.json().get("ok"):
            print("Telegram notification sent!")
            return True

    except Exception as error:
        logger.error("Telegram notification failed: %s", type(error).__name__)

    return False