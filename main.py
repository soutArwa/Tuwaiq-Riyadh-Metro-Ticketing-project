import sys
from Metro_admin_section.Metro_Data import Stations, show_lines, get_ticket_price
from Metro_admin_section.Adminstrative import handle_change_price, toggle_line_status
from Metro_admin_section.Student_Discount import apply_student_discount
from Metro_admin_section.Invoice import generate_invoice_file

ADMIN_PIN = "4123"
cart = []

print("========================================")
print("      Welcome to Riyadh Metro CLI       ")
print("========================================")

passenger_name = input("Enter your name to start: ").strip()

print(f"\nWelcome, {passenger_name}!")

while True:
    """While the user did not chose to exit, the code will complete on running"""
    print("\n----------------------------------------")
    print("Main Menu:")
    print("1. Browse all Metro lines")
    print("2. Check route details of a line")
    print("3. Purchase a ticket")
    print(f"4. View cart and checkout ({len(cart)} items)")
    print("5. Manager mode")
    print("6. Exit")
    print("----------------------------------------")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        show_lines()


    elif choice == "2":
        line_id = input("\nEnter line number (1-6): ").strip()
        if line_id in Stations:
            print(f"\nLine Name: {Stations[line_id]['name']}")
            print(f"Route: {Stations[line_id]['description']}")
            print(f"Status: {Stations[line_id].get('status', 'Active')}")
        else:
            print("Invalid line number. Please enter a number between 1 and 6")

    
    elif choice == "3":
        show_lines()
        line_id = input("Enter line number to book (1-6): ").strip()
        if line_id not in Stations:
            print("Invalid line number.")
            continue

        
        if Stations[line_id].get("status") == "Maintenance":
            print(f"\n⚠️ Sorry, {Stations[line_id]['name']} is currently under maintenance and cannot be booked.")
            continue

        duration = input("Enter duration (daily/monthly/yearly): ").strip().lower()
        tier = input("Enter class (economy/first_class): ").strip().lower()

        price = get_ticket_price(line_id, duration, tier)
        if price is None:
            continue

        print(f"\nStandard price: {price} SAR")

        discount_amount = 0
        student_info = None
        is_student = input("\nAre you a university student? (yes/no): ").strip().lower()
        if is_student in ["yes", "y"]:
            discount_amount, student_info = apply_student_discount(price)

        final_ticket_price = price - discount_amount
        cart.append({
            "line_name": Stations[line_id]["name"],
            "duration": duration,
            "tier": tier,
            "price": final_ticket_price,
            "student_info": student_info,
            "original_price": price,
            "discount": discount_amount,
        })
        print(f"\nTicket added to cart successfully! Price: {final_ticket_price} SAR.")

    
    elif choice == "4":
        if not cart:
            print("\nYour cart is empty.")
            continue

        print("\n--- Items in Cart ---")
        total_sum = sum(item["price"] for item in cart)
        for item in cart:
            print(f"- {item['line_name']} ({item['tier']} - {item['duration']}): {item['price']} SAR")
        print(f"Total Amount: {total_sum} SAR\n")

        confirm_pay = input("Do you want to checkout and pay? (yes/no): ").strip().lower()
        if confirm_pay in ["yes", "y"]:
            student_data = cart[0].get("student_info")
            total_orig = sum(item["original_price"] for item in cart)
            total_disc = sum(item["discount"] for item in cart)

            generate_invoice_file(passenger_name, cart, total_orig, total_disc, total_sum, student_data)
            cart.clear()
            print(f"\nCheckout completed successfully. Thank you, {passenger_name}!")
        else:
            print("Checkout cancelled.")

    
    elif choice == "5":
        pin = input("\nEnter Admin PIN: ").strip()
        if pin == ADMIN_PIN:
            print("\nManager Panel:")
            print("1. Change ticket price")
            print("2. Toggle line maintenance status")
            admin_choice = input("Select option (1-2): ").strip()

            if admin_choice == "1":
                handle_change_price()
            elif admin_choice == "2":
                toggle_line_status()
            else:
                print("Invalid choice")
        else:
            print("Wrong PIN")

    elif choice == "6":
        print(f"\nThank you for using Riyadh Metro, {passenger_name}. Goodbye!")
        sys.exit()

    else:
        print("Invalid choice, please enter a number from 1 to 6")