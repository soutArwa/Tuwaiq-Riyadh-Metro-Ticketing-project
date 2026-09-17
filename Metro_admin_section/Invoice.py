import datetime


def generate_invoice_file(customer_name, cart, subtotal, discount_amount, final_total, student_info=None):
    """Generates and writes a formatted invoice to a text file"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Invoice_{customer_name}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("=========================================\n")
        file.write("           RIYADH METRO INVOICE          \n")
        file.write("=========================================\n")
        file.write(f"Customer Name : {customer_name}\n")
        file.write(f"Date & Time   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        if student_info:
            file.write("Passenger Type: Student (50% Discount Applied)\n")
            file.write(f"University    : {student_info['university']}\n")
            file.write(f"Student ID    : {student_info['student_id']}\n")
        else:
            file.write("Passenger Type: Standard\n")

        file.write("-----------------------------------------\n")
        file.write("Booked Trips:\n")
        for item in cart:
            file.write(f"- {item['line_name']} | {item['tier'].title()} | {item['duration'].title()} : {item['price']} SAR\n")

        file.write("-----------------------------------------\n")
        file.write(f"Subtotal      : {subtotal} SAR\n")
        file.write(f"Discount      : -{discount_amount} SAR\n")
        file.write(f"Total Paid    : {final_total} SAR\n")
        file.write("=========================================\n")
        file.write("Thank you for using Riyadh Metro!\n")

    print(f"\nOfficial Invoice generated successfully: '{filename}'")
    return filename