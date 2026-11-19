# ✈️ Flight Price Tracker

A Python-based Flight Price Tracker that searches for flights, compares ticket prices with user-defined target prices, and sends email notifications when flights are available within the budget.

The application uses the SerpAPI Google Flights engine to retrieve flight information and SQLite to store destination details. It also supports automatic price monitoring using APScheduler.

## Features

- **Flight Search:** Search for flights using origin, destination, and travel date.
- **Airport Validation:** Validate airport codes using a local airport dataset.
- **Destination Management:** Add, update, and delete saved destinations.
- **Price Comparison:** Compare current flight prices with target prices.
- **Lowest Price Tracking:** Keep track of the lowest price found for each destination.
- **Email Notifications:** Receive email alerts when a flight is within your target budget.
- **Automatic Monitoring:** Automatically check flight prices every 10 hours.
- **Database Storage:** Store destination information using SQLite.
- **Input Validation:** Validate airport codes, prices, destination IDs, and travel dates.
- **Logging:** Record application events and errors.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SQLite | Database management |
| SerpAPI | Google Flights search |
| Requests | API communication |
| APScheduler | Automated flight monitoring |
| SMTP | Email notifications |
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
│   ├── test_airport_data.py
│   ├── test_database.py
│   ├── test_flight_data.py
│   ├── test_price_tracker.py
│   └── manual_flight_search.py
│
├── logs/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/pallavikambali/flight-price-tracker.git
```

```bash
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
pip install -r requirements.txt
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
```

**API Configuration:**

- Obtain a SerpAPI API key to search for flights.
- Configure your SMTP