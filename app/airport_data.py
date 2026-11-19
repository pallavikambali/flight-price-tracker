import csv
from pathlib import Path

AIRPORT_FILE = Path(__file__).parent.parent / "data" / "airports.csv"


def load_airport_codes():
    valid_codes = set()

    with open(AIRPORT_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if (
                row["iata_code"]
                and row["scheduled_service"] == "yes"
                and row["type"] in [
                    "large_airport",
                    "medium_airport",
                    "small_airport"
                ]
            ):
                valid_codes.add(row["iata_code"])

    return valid_codes


VALID_AIRPORT_CODES = load_airport_codes()


def is_valid_airport(code):
    return code in VALID_AIRPORT_CODES