from apscheduler.schedulers.background import BackgroundScheduler


def check_flight_prices():

    from app.flight_monitor import search_flight_prices

    print("\n[Scheduler] Starting automatic flight price monitoring...")

    search_flight_prices()

    print("[Scheduler] Flight price monitoring completed.")


def start_scheduler():

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        func=check_flight_prices,
        trigger="interval",
        hours=10,
        id="flight_price_monitor"
    )

    scheduler.start()

    print("Automatic flight monitoring started!")

    return scheduler