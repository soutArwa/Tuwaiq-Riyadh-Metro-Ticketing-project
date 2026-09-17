from Metro_admin_section.Metro_Data import Stations, prices, show_lines, save_data


def toggle_line_status():
    """Allows an admin to change the operational status of a metro line."""
    show_lines()
    line_id = input("Enter line number to change status (1-6): ").strip()

    if line_id not in Stations:
        print("Invalid line selection.")
        return False

    current_status = Stations[line_id].get("status", "Active")
    new_status = "Maintenance" if current_status == "Active" else "Active"

    Stations[line_id]["status"] = new_status
    save_data()  
    print(f"\nSuccess: {Stations[line_id]['name']} status changed to '{new_status}'.")
    return True


def change_price(duration, name_of_class, price):
    """Allows an admin to change price of classes within the allowed range (4 to 5000 SAR)."""
    if price < 4 or price > 5000:
        print("Please enter a reasonable number between 4 and 5000.")
        return False

    if duration not in prices or name_of_class not in prices[duration]:
        print(f"Error: Invalid duration '{duration}' or class tier '{name_of_class}'.")
        return False

    prices[duration][name_of_class] = price
    for line_id in Stations:
        Stations[line_id]["prices"][duration][name_of_class] = price
        
    save_data()  
    print(f"\nSuccess: Price for {name_of_class} ({duration}) updated to {price} SAR.")
    return True


def handle_change_price():
    """Handles terminal input and triggers change_price safely."""
    dur = input("Enter duration (daily/monthly/yearly): ").strip().lower()
    tier = input("Enter class (economy/first_class): ").strip().lower()
    try:
        new_price = int(input("Enter new price (4-5000 SAR): ").strip())
        change_price(dur, tier, new_price)
    except ValueError:
        print("Price must be a number.")