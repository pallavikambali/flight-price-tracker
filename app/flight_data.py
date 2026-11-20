from app.logger import logger


def extract_flight_data(data, connecting_only=False):

    flights = data.get("best_flights", []) + data.get("other_flights", [])

    valid_flights = [
        flight for flight in flights
        if isinstance(flight, dict)
        and isinstance(flight.get("price"), (int, float))
        and flight.get("flights")
    ]

    if connecting_only:
        valid_flights = [
            flight for flight in valid_flights
            if len(flight["flights"]) > 1
        ]

    if not valid_flights:
        logger.warning("No valid flight records found")
        return None

    cheapest_flight = min(
        valid_flights,
        key=lambda flight: flight["price"]
    )

    flight_segments = cheapest_flight["flights"]

    first_leg = flight_segments[0]
    last_leg = flight_segments[-1]

    return {
        "origin": first_leg["departure_airport"]["id"],
        "destination": last_leg["arrival_airport"]["id"],
        "price": cheapest_flight["price"],
        "airline": first_leg["airline"],
        "flight_number": first_leg["flight_number"],
        "duration": cheapest_flight["total_duration"],
        "stops": len(flight_segments) - 1
    }
