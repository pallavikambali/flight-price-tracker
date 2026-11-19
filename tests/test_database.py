import app.database as database


def test_database_operations(tmp_path, monkeypatch):
    # Use a temporary database instead of our actual database
    test_db = tmp_path / "test.db"
    monkeypatch.setattr(database, "DATABASE_PATH", str(test_db))

    # Create the database table
    database.initialize_database()

    # 1. Add a destination
    database.add_destination("BLR", "DEL", 5000, "2026-12-15")

    # 2. Retrieve destinations
    destinations = database.get_destinations()

    assert len(destinations) == 1
    assert destinations[0][1] == "BLR"
    assert destinations[0][2] == "DEL"
    assert destinations[0][3] == 5000
    assert destinations[0][6] == "2026-12-15"

    destination_id = destinations[0][0]

    # 3. Update the lowest price
    database.update_lowest_price(destination_id, 4500)

    destinations = database.get_destinations()
    assert destinations[0][4] == 4500

    # 4. Mark alert as sent
    database.mark_alert_sent(destination_id)

    destinations = database.get_destinations()
    assert destinations[0][5] == 1

    # 5. Update the target price
    database.update_target_price(destination_id, 4000)

    destinations = database.get_destinations()
    assert destinations[0][3] == 4000
    assert destinations[0][5] == 0

    # 6. Delete the destination
    deleted = database.delete_destination(destination_id)

    assert deleted is True
    assert database.get_destinations() == []