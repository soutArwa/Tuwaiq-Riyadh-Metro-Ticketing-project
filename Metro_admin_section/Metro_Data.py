import json
import os

prices = {
    "daily": {"economy": 4, "first_class": 10},
    "monthly": {"economy": 140, "first_class": 350},
    "yearly": {"economy": 1260, "first_class": 3150},
}

default_stations = {
    "1": {
        "name": "Blue Line",
        "description": "SAB Bank ↔ Ad Dar Al Baida — 25 stations across 38.0 km",
        "status": "Active",
        "prices": prices,
    },
    "2": {
        "name": "Red Line",
        "description": "King Saud University ↔ King Fahad Sport City — 15 stations across 25.3 km",
        "status": "Active",
        "prices": prices,
    },
    "3": {
        "name": "Orange Line",
        "description": "Jeddah Road ↔ Khashm Al An — 22 stations across 40.7 km",
        "status": "Active",
        "prices": prices,
    },
    "4": {
        "name": "Yellow Line",
        "description": "Ministry of Education ↔ National Museum — 12 stations across 12.9 km",
        "status": "Active",
        "prices": prices,
    },
    "5": {
        "name": "Green Line",
        "description": "Ministry of Education ↔ National Museum — 12 stations across 12.9 km",
        "status": "Active",
        "prices": prices,
    },
    "6": {
        "name": "Purple Line",
        "description": "Connect north Riyadh directly with the east without passing through the city centre",
        "status": "Active",
        "prices": prices,
    },
}

DATA_FILE = "metro_data.json"

def save_data():
     with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(Stations, f, ensure_ascii=False, indent=4)

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return default_stations
    return default_stations


Stations = load_data()


def show_lines():
    """Iterates through the Stations dictionary and displays each metro line with its route and status"""
    print("\n--- Riyadh Metro Lines ---")
    for key, line in Stations.items():
        status = line.get("status", "Active")
        print(f"[{key}] {line['name']} - [{status}]")
        print(f"    Route: {line['description']}")
    print("--------------------------\n")


def get_ticket_price(line_id, duration, tier):
    """
    Validates line ID and retrieves the ticket price based on selected duration and type of class.
    Returns the integer price if valid, or None if inputs are invalid.
    """
    if line_id not in Stations:
        print("Invalid line selection. Please choose a line between (1 - 6)")
        return None

    try:
        price = Stations[line_id]["prices"][duration][tier]
        return price
    except KeyError:
        print("Invalid duration or class selected.")
        return None