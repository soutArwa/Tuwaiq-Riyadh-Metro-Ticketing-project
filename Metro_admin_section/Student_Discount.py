UNIVERSITIES = {
    "1": "King Saud University",
    "2": "Princess Nourah University",
    "3": "Imam Mohammad Ibn Saud Islamic University",
    "4": "King Saud bin Abdulaziz University for Health Sciences",
    "5": "Prince Sultan University",
    "6": "Alfaisal University",
    "7": "Al Yamamah University",
    "8": "Dar Al Uloom University",
}


def show_universities():
    """Displays the list of eligible universities"""
    print("\n--- Eligible Universities for Student Discount (50% OFF) ---")
    for key, name in UNIVERSITIES.items():
        print(f"[{key}] {name}")
    print("-------------------------------------------------------------")


def verify_student(uni_choice, student_id):
    """
    Validates university selection and student ID format.
    Ensures ID is numeric and has a valid length (6 to 10 digits)
    """
    if uni_choice not in UNIVERSITIES:
        print("Invalid university selection")
        return False, None

    cleaned_id = student_id.strip()
    if not cleaned_id.isdigit() or not (6 <= len(cleaned_id) <= 10):
        print("Invalid Student ID format. Must be 6-10 digits.")
        return False, None

    uni_name = UNIVERSITIES[uni_choice]
    return True, uni_name


def apply_student_discount(price):
    """checks university and student ID to apply a 50% discount."""
    show_universities()
    while True:
        uni_choice = input("Enter university number (or type 'exit' to cancel): ").strip()
        if uni_choice.lower() == "exit":
            print("Student discount cancelled.")
            return 0, None

        student_id = input("Enter student ID (or type 'exit' to cancel): ").strip()
        if student_id.lower() == "exit":
            print("Student discount cancelled.")
            return 0, None

        is_valid, uni_name = verify_student(uni_choice, student_id)
        if is_valid:
            discount_amount = price * 0.50
            student_info = {
                "university": uni_name,
                "student_id": student_id,
            }
            print(f"Discount applied: 50% off via {uni_name}.")
            return discount_amount, student_info
        else:
            print("Invalid university or ID. Try again or type 'exit'.\n")