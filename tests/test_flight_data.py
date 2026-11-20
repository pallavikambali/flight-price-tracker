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

def test_direct_flight_has_zero_stops():

    data = {
        "best_flights": [
            {
                "price": 5000,
                "flights": [
                    {
                        "departure_airport": {"id": "BLR"},
                        "arrival_airport": {"id": "DEL"},
                        "airline": "IndiGo",
                        "flight_number": "6E 123"
                    }
                ],
                "total_duration": 150
            }
        ]
    }

    flight = extract_flight_data(data)

    assert flight["stops"] == 0

def test_connecting_flight_has_one_stop():

    data = {
        "best_flights": [
            {
                "price": 6500,
                "flights": [
                    {
                        "departure_airport": {"id": "BLR"},
                        "arrival_airport": {"id": "HYD"},
                        "airline": "IndiGo",
                        "flight_number": "6E 101"
                    },
                    {
                        "departure_airport": {"id": "HYD"},
                        "arrival_airport": {"id": "DEL"},
                        "airline": "IndiGo",
                        "flight_number": "6E 202"
                    }
                ],
                "total_duration": 240
            }
        ]
    }

    flight = extract_flight_data(data, connecting_only=True)

    assert flight["price"] == 6500
    assert flight["stops"] == 1
    assert flight["origin"] == "BLR"
    assert flight["destination"] == "DEL"

def test_no_connecting_flights():

    data = {
        "best_flights": [
            {
                "price": 5000,
                "flights": [
                    {
                        "departure_airport": {"id": "BLR"},
                        "arrival_airport": {"id": "DEL"},
                        "airline": "IndiGo",
                        "flight_number": "6E 123"
                    }
                ],
                "total_duration": 150
            }
        ]
    }

    flight = extract_flight_data(data, connecting_only=True)

    assert flight is None