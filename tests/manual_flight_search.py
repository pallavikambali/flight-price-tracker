from app.flight_search import search_flights

data = search_flights("BLR", "DEL", "2026-12-20")

if data:
    print(data.keys())
    print(data.get("best_flights"))