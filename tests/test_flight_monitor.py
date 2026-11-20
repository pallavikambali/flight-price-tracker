from app.flight_monitor import select_cheapest_flight
from unittest.mock import patch


def test_direct_flight_is_selected():

    direct_flight = {
        "origin": "BLR",
        "destination": "DEL",
        "price": 5000,
        "airline": "IndiGo",
        "flight_number": "6E 123",
        "duration": 150,
        "stops": 0
    }

    with patch(
        "app.flight_monitor.search_flights",
        return_value={"best_flights": [{"price": 5000, "flights": [
            {
                "departure_airport": {"id": "BLR"},
                "arrival_airport": {"id": "DEL"},
                "airline": "IndiGo",
                "flight_number": "6E 123"
            }
        ], "total_duration": 150}]}
    ) as mock_search:

        flight = select_cheapest_flight("BLR", "DEL", "2026-12-20", 6000)

        assert flight["price"] == 5000
        assert flight["stops"] == 0

        # Connecting search should not happen
        assert mock_search.call_count == 1


def test_cheaper_connecting_flight_is_selected():

    direct_data = {
        "best_flights": [
            {
                "price": 8000,
                "flights": [
                    {
                        "departure_airport": {"id": "BLR"},
                        "arrival_airport": {"id": "DEL"},
                        "airline": "Air India",
                        "flight_number": "AI 123"
                    }
                ],
                "total_duration": 150
            }
        ]
    }

    connecting_data = {
        "best_flights": [
            {
                "price": 5500,
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

    with patch(
        "app.flight_monitor.search_flights",
        side_effect=[direct_data, connecting_data]
    ):

        flight = select_cheapest_flight(
            "BLR", "DEL", "2026-12-20", 6000
        )

        assert flight["price"] == 5500
        assert flight["stops"] == 1


def test_connecting_flight_selected_when_no_direct_flight():

    direct_data = {"best_flights": []}

    connecting_data = {
        "best_flights": [
            {
                "price": 5500,
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

    with patch(
        "app.flight_monitor.search_flights",
        side_effect=[direct_data, connecting_data]
    ):

        flight = select_cheapest_flight(
            "BLR", "DEL", "2026-12-20", 6000
        )

        assert flight is not None
        assert flight["price"] == 5500
        assert flight["stops"] == 1
