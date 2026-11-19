from app.database import (
    get_destinations,
    add_destination,
    update_target_price,
    delete_destination
)

from app.validators import (
    get_valid_airport_code,
    get_valid_price,
    get_valid_id,
    get_valid_date
)


def add_destination_menu():
    print("\n--- Add New Destination ---")

    origin = get_valid_airport_code("Enter origin airport code: ")
    destination = get_valid_airport_code("Enter destination airport code: ")

    if origin == destination:
        print("Origin and destination cannot be the same!")
        return

    target_price = get_valid_price()
    travel_date = get_valid_date()

    add_destination(origin, destination, target_price, travel_date)

    print("Destination added successfully!")


def update_destination_menu():
    destinations = get_destinations()

    if not destinations:
        print("No destinations available.")
        return

    print("\n--- Your Destinations ---")

    for destination in destinations:
        print(
            f"ID: {destination[0]} | "
            f"{destination[1]} → {destination[2]} | "
            f"Target: ₹{destination[3]}"
        )

    destination_id = get_valid_id("\nEnter destination ID: ")

    new_price = get_valid_price()
    update_target_price(destination_id, new_price)

    print("Target price updated successfully!")


def delete_destination_menu():
    destinations = get_destinations()

    if not destinations:
        print("No destinations available.")
        return

    print("\n--- Your Destinations ---")

    for destination in destinations:
        print(
            f"ID: {destination[0]} | "
            f"{destination[1]} → {destination[2]} | "
            f"Target: ₹{destination[3]}"
        )

    destination_id = get_valid_id("\nEnter destination ID to delete: ")

    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":
        deleted = delete_destination(destination_id)

        if deleted:
            print("Destination deleted successfully!")
        else:
            print("No destination found with that ID!")

    else:
        print("Deletion cancelled.")