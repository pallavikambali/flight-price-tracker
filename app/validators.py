import re
from datetime import datetime
from app.airport_data import is_valid_airport


def get_valid_airport_code(prompt):
    while True:
        code = input(prompt).strip().upper()

        if not re.fullmatch(r"[A-Z]{3}", code):
            print("Invalid format! Enter exactly 3 letters.")
            continue

        if is_valid_airport(code):
            return code

        print("Airport code not found in our database!")


def get_valid_price():
    while True:
        try:
            price = float(input("Enter your target price: "))

            if price > 0:
                return price

            print("Price must be greater than zero!")

        except ValueError:
            print("Please enter a valid number!")


def get_valid_id(prompt):
    while True:
        try:
            destination_id = int(input(prompt))

            if destination_id > 0:
                return destination_id

            print("ID must be greater than zero!")

        except ValueError:
            print("Please enter a valid numeric ID!")


def get_valid_date():
    while True:
        outbound_date = input("Enter travel date (YYYY-MM-DD): ")

        try:
            travel_date = datetime.strptime(outbound_date, "%Y-%m-%d")

            if travel_date.strftime("%Y-%m-%d") != outbound_date:
                print("Please enter date in YYYY-MM-DD format.")
                continue

            if travel_date.date() < datetime.today().date():
                print("Travel date cannot be in the past!")
                continue

            return outbound_date

        except ValueError:
            print("Invalid date! Please use YYYY-MM-DD format.")