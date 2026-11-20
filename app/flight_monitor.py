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

        data = search_flights(origin, destination_code, outbound_date)

        if data is None:
            continue

        flight = extract_flight_data(data)

        if flight is None:
            print("No flights found.")
            continue
        print("\nCheapest flight found:")
        print(f"Airline: {flight['airline']}")
        print(f"Flight: {flight['flight_number']}")
        print(f"Price: ₹{flight['price']}")

        check_price(flight, target_price, lowest_price)

        if flight["price"] <= target_price and alert_sent == 0:

            email_sent = send_notification(flight, target_price)
            telegram_sent = send_telegram_notification(flight, target_price)

            if email_sent or telegram_sent:
                mark_alert_sent(destination_id)
                
        if lowest_price is None or flight["price"] < lowest_price:
            update_lowest_price(destination_id, flight["price"])
            print("New lowest price recorded!")