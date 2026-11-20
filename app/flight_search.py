import requests
from app.config import SERPAPI_KEY
from app.logger import logger

def search_flights(origin, destination, outbound_date, stops=None):
    api_url = "https://serpapi.com/search"

    params = {
        "engine": "google_flights",
        "departure_id": origin,
        "arrival_id": destination,
        "outbound_date": outbound_date,
        "type": "2",
        "currency": "INR",
        "gl": "in",
        "hl": "en",
        "api_key": SERPAPI_KEY
    }

    if stops is not None:
        params["stops"] = stops

    logger.info("Searching flights: %s → %s", origin, destination)

    try:
        response = requests.get(api_url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        logger.info("Flight search completed successfully")
        return data

    except requests.exceptions.RequestException as error:
        logger.error("Flight search failed: %s", type(error).__name__)
        print(f"Flight search failed: {type(error).__name__}")
        return None
