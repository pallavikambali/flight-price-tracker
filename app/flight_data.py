from app.logger import logger


def extract_flight_data(data):
    flights = data.get("best_flights", [])

    # Keep only flight records with a valid price and flight details
    valid_flights = [
        flight for flight in flights
        if isinstance(flight, dict)
        and isinstance(flight.get("price"), (int, float))
        and flight.get("flights")
    ]

    if not valid_flights:
        logger.warning("No valid flight records found")
        return None

    cheapest_flight = min(
        valid_flights,
        key=lambda flight: flight["price"]
    )

    first_leg = cheapest_flight["flights"][0]
    last_leg = cheapest_flight["flights"][-1]

    return {
        "origin": first_leg["departure_airport"]["id"],
        "destination": last_leg["arrival_airport"]["id"],
        "price": cheapest_flight["price"],
        "airline": first_leg["airline"],
        "flight_number": first_leg["flight_number"],
        "duration": cheapest_flight["total_duration"]
    }