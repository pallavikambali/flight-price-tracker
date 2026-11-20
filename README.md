# ✈️ Flight Price Tracker

A Python-based Flight Price Tracker that searches for flights, compares ticket prices against user-defined budgets, and sends email and Telegram notifications when cheaper flights are found.

The application uses the SerpAPI Google Flights engine to retrieve flight information, SQLite to store destination details, and APScheduler to automate flight price monitoring.

## Features

- **Flight Search:** Search for flights using origin, destination, and travel date.
- **Direct Flight Search:** Search for direct flights first.
- **Connecting Flight Fallback:** Search for connecting flights when direct flights are unavailable or exceed the target price.
- **Airport Validation:** Validate airport codes using a local airport dataset.
- **Destination Management:** Add, update, and delete saved destinations.
- **Price Comparison:** Compare flight prices with user-defined target prices.
- **Lowest Price Tracking:** Record the lowest price found for each destination.
- **Email Notifications:** Receive email alerts when flights meet your budget.
- **Telegram Notifications:** Receive flight price alerts through a Telegram bot.
- **Automatic Monitoring:** Automatically monitor flight prices every 10 hours.
- **Database Storage:** Store destination information using SQLite.
- **Input Validation:** Validate airport codes, prices, destination IDs, and travel dates.
- **Logging:** Record application events and errors.
- **Automated Testing:** Test important application functionality using Pytest.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SQLite | Database management |
| SerpAPI | Google Flights search |
| Requests | API communication |
| APScheduler | Automated flight monitoring |
| SMTP | Email notifications |
| Telegram Bot API | Telegram notifications |
| python-dotenv | Environment variable management |
| Pytest | Automated testing |

## Project Structure

```text
flight-price-tracker/
│
├── app/
│   ├── __init__.py
│   ├── airport_data.py
│   ├── config.py
│   ├── database.py
│   ├── destination_manager.py
│   ├── flight_data.py
│   ├── flight_monitor.py
│   ├── flight_search.py
│   ├── logger.py
│   ├── main.py
│   ├── notification_manager.py
│   ├── price_tracker.py
│   ├── scheduler.py
│   └── validators.py
│
├── data/
│   └── airports.csv
│
├── tests/
│   ├── __init__.py
│   ├── manual_flight_search.py
│   ├── test_airport_data.py
│   ├── test_database.py
│   ├── test_flight_data.py
│   ├── test_flight_monitor.py
│   └── test_price_tracker.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/pallavikambali/flight-price-tracker.git
cd flight-price-tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

**Linux / Ubuntu:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a reference.

Configure the following variables:

```env
APP_ENV=development

SERPAPI_KEY=your_serpapi_api_key

DATABASE_PATH=data/flights.db

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password
NOTIFICATION_EMAIL=recipient_email@gmail.com

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

**API and notification configuration:**

- Obtain a SerpAPI API key for flight searches.
- Configure Gmail SMTP using an app password.
- Create a Telegram bot using BotFather.
- Add your Telegram bot token and chat ID.

Keep your actual `.env` file private. Never upload API keys, passwords, or bot tokens to GitHub.

## Running the Application

Start the application using:

```bash
python -m app.main
```

Use the interactive menu to manage destinations and search for flight prices.

The application can also monitor saved destinations automatically using APScheduler.

## Running Tests

Run the automated test suite:

```bash
python -m pytest -v
```

The tests cover:

- Airport code validation
- Database operations
- Flight data extraction
- Direct and connecting flight selection
- Connecting flight fallback
- Price comparison and tracking

## Future Improvements

- Support for additional flight search providers.
- Improved flight search filters.
- More detailed flight information and comparisons.

## Author

**Pallavi Kambali**

GitHub: pallavikambali