from app.database import (
    get_destinations,
    update_lowest_price,
    mark_alert_sent
)

from app.flight_search import search_flights
from app.flight_data import extract_flight_data
from app.price_tracker import check_price
from app.notification_manager import (
    send_notification,
    send_telegram_notification
)
def select_cheapest_flight(origin, destination, outbound_date, target_price):

    # Search direct flights first
    data = search_flights(
        origin, destination, outbound_date, stops=1
    )

    if data is None:
        return None

    flight = extract_flight_data(data)

    # Search connecting flights if necessary
    if flight is None or flight["price"] > target_price:

        print("Searching for connecting flights...")

        connecting_data = search_flights(
            origin, destination, outbound_date, stops=2
        )

        if connecting_data is not None:

            connecting_flight = extract_flight_data(
                connecting_data,
                connecting_only=True
            )

            if connecting_flight is not None:

                if flight is None or connecting_flight["price"] < flight["price"]:
                    flight = connecting_flight

    return flight



def search_flight_prices():

    destinations = get_destinations()

    if not destinations:
        print("No destinations added yet.")
        return

    for destination in destinations:

        destination_id, origin, destination_code, target_price, lowest_price, alert_sent, outbound_date = destination

        if outbound_date is None:
            print(f"Travel date not set for {origin} → {destination_code}")
            continue

        print(f"\nSearching flights: {origin} → {destination_code}")

        # Step 1: Search direct flights
        flight = select_cheapest_flight(
            origin,
            destination_code,
            outbound_date,
            target_price
        )

        if flight is None:
            print("No flights found.")
            continue

        # Step 3: Display cheapest flight
        print("\nCheapest flight found:")
        print(f"Airline: {flight['airline']}")
        print(f"Flight: {flight['flight_number']}")
        print(f"Stops: {flight['stops']}")
        print(f"Price: ₹{flight['price']}")

        # Step 4: Check price
        check_price(flight, target_price, lowest_price)

        # Step 5: Send notifications
        if flight["price"] <= target_price and alert_sent == 0:

            email_sent = send_notification(flight, target_price)
            telegram_sent = send_telegram_notification(flight, target_price)

            if email_sent or telegram_sent:
                mark_alert_sent(destination_id)

        # Step 6: Update lowest price
        if lowest_price is None or flight["price"] < lowest_price:

            update_lowest_price(destination_id, flight["price"])
            print("New lowest price recorded!")
