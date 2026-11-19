from app.flight_data import extract_flight_data


def test_extract_cheapest_flight():
    data = {
        "best_flights": [
            {
                "price": 9000,
                "flights": [
                    {
                        "departure_airport": {"id": "BLR"},
                        "arrival_airport": {"id": "DEL"},
                        "airline": "Air India",
                        "flight_number": "AI 123"
                    }
                ],
                "total_duration": 150
            },
            {
                "price": 7000,
                "flights": [
                    {
                        "departure_airport": {"id": "BLR"},
                        "arrival_airport": {"id": "DEL"},
                        "airline": "IndiGo",
                        "flight_number": "6E 456"
                    }
                ],
                "total_duration": 140
            }
        ]
    }

    flight = extract_flight_data(data)

    assert flight["price"] == 7000
    assert flight["airline"] == "IndiGo"
    assert flight["flight_number"] == "6E 456"


def test_no_flights_found():
    data = {"best_flights": []}

    flight = extract_flight_data(data)

    assert flight is None