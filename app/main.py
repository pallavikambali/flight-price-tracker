from app.database import initialize_database
from app.scheduler import start_scheduler

from app.destination_manager import (
    add_destination_menu,
    update_destination_menu,
    delete_destination_menu
)

from app.flight_monitor import search_flight_prices


def show_menu():

    print("\n===== FLIGHT PRICE TRACKER =====")
    print("1. Add destination")
    print("2. Update target price")
    print("3. Delete destination")
    print("4. Search flight prices")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    return choice


def main():

    initialize_database()
    scheduler = start_scheduler()

    print("Welcome to Flight Price Tracker!")

    try:
        while True:

            choice = show_menu()

            if choice == "1":
                add_destination_menu()

            elif choice == "2":
                update_destination_menu()

            elif choice == "3":
                delete_destination_menu()

            elif choice == "4":
                search_flight_prices()

            elif choice == "5":
                print("Thank you for using Flight Price Tracker!")
                break

            else:
                print("Invalid choice! Please try again.")

    finally:
        scheduler.shutdown(wait=False)
        print("Flight monitoring scheduler stopped.")


if __name__ == "__main__":
    main()