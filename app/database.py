import sqlite3
from pathlib import Path

from app.config import DATABASE_PATH


def get_connection():
    # Create the data folder if it doesn't exist
    Path(DATABASE_PATH).parent.mkdir(parents=True, exist_ok=True)

    # Connect to the SQLite database
    connection = sqlite3.connect(DATABASE_PATH)

    return connection


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS destinations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            origin TEXT NOT NULL,
            destination TEXT NOT NULL,
            target_price REAL NOT NULL,
            lowest_price REAL,
            alert_sent INTEGER NOT NULL DEFAULT 0
        )
    """)

    cursor.execute("PRAGMA table_info(destinations)")
    columns = [column[1] for column in cursor.fetchall()]

    if "alert_sent" not in columns:
        cursor.execute("""
            ALTER TABLE destinations
            ADD COLUMN alert_sent INTEGER NOT NULL DEFAULT 0
        """)

    if "travel_date" not in columns:
        cursor.execute("""
            ALTER TABLE destinations
            ADD COLUMN travel_date TEXT
        """)

    connection.commit()
    connection.close()


def add_destination(origin, destination, target_price, travel_date):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO destinations (origin, destination, target_price, travel_date)
        VALUES (?, ?, ?, ?)
    """, (origin, destination, target_price, travel_date))

    connection.commit()
    connection.close()


def get_destinations():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, origin, destination, target_price,
               lowest_price, alert_sent, travel_date
        FROM destinations
    """)

    destinations = cursor.fetchall()
    connection.close()

    return destinations


def update_lowest_price(destination_id, new_price):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE destinations
        SET lowest_price = ?
        WHERE id = ?
    """, (new_price, destination_id))

    connection.commit()
    connection.close()


def delete_destination(destination_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM destinations
        WHERE id = ?
    """, (destination_id,))

    deleted = cursor.rowcount

    connection.commit()
    connection.close()

    return deleted > 0


def mark_alert_sent(destination_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE destinations
        SET alert_sent = 1
        WHERE id = ?
    """, (destination_id,))

    connection.commit()
    connection.close()


def update_target_price(destination_id, new_target_price):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE destinations
        SET target_price = ?, alert_sent = 0
        WHERE id = ?
    """, (new_target_price, destination_id))

    connection.commit()
    connection.close()