# Riyadh Metro Ticketing & Route Management CLI

## Overview

An interactive command-line ticketing and route management system for the **Riyadh Metro** network.

The system serves two primary roles:

* **Passengers** can browse metro lines, check operational status, view routes, calculate fares with student discounts, manage their cart, and checkout with an exported invoice.
* **Station Managers** can manage ticket pricing tariffs and toggle line maintenance status to suspend or resume bookings.

---

## Features & User Stories

### As a Passenger, I should be able to:

* **Browse all available lines:** View all lines, terminal stations, and operational status (`Active` / `Maintenance`).
* **Check line details:** View the full route details for any specific line from 1 to 6.
* **Book metro tickets:** Select an active line, ticket duration (`Daily`, `Monthly`, `Yearly`), and class tier (`Economy`, `First Class`).
* **Apply student discounts:** Verify university enrollment and student ID to receive a **50% discount**.
* **Manage cart:** Add tickets to the cart and view itemized order totals.
* **Checkout and pay:** Confirm the passenger name and generate an official text invoice receipt.

### As a Manager, I should be able to:

* **Authenticate securely:** Access the Manager Dashboard using an Admin PIN.
* **Update ticket pricing:** Modify tariff prices for any duration and class tier within the allowed price range.
* **Toggle line status:** Switch a line between `Active` and `Maintenance` to halt or resume ticket bookings.

---

## Project Structure

```text
Riyadh_Metro_Project/
├── main.py
├── Metro_admin_section/
│   ├── __init__.py
│   ├── Metro_Data.py
│   ├── Adminstrative.py
│   ├── Student_Discount.py
│   └── Invoice.py
├── requirements.txt
└── README.md
```

### File Description

| File / Directory      | Description                                                                 |
| --------------------- | --------------------------------------------------------------------------- |
| `main.py`             | Application entry point and interactive CLI menu                            |
| `Metro_Data.py`       | Stores metro lines, station information, statuses, and pricing              |
| `Adminstrative.py`    | Handles administrative controls such as pricing updates and status toggling |
| `Student_Discount.py` | Handles academic verification and student discount processing               |
| `Invoice.py`          | Generates file-based ticket receipts                                        |
| `requirements.txt`    | Lists project dependencies                                                  |
| `README.md`           | Project documentation and usage guide                                       |

---

## Usage

### 1. Run the Project

Execute the entry file from the project root:

```bash
python main.py
```

---

### 2. Commands & Navigation

After running the application, the user can navigate through the following options:

| Option     | Description                                                               |
| ---------- | ------------------------------------------------------------------------- |
| `Start`    | Enter your name to initiate an interactive personalized session           |
| `Option 1` | Browse all metro lines, route coverage, and operational status            |
| `Option 2` | Inspect specific line details by line number                              |
| `Option 3` | Book a ticket with status checking and student discount verification      |
| `Option 4` | Review shopping cart items and complete checkout with an exported invoice |
| `Option 5` | Access Manager Mode to update prices or toggle maintenance status         |
| `Option 6` | Exit the CLI application safely                                           |

---

## Ticket Options

Passengers can select from:

### Duration

* Daily
* Monthly
* Yearly

### Class

* Economy
* First Class

### Student Discount

Eligible students can receive a **50% discount** after completing the required university enrollment and student ID verification.

---

## Manager Mode

Manager Mode provides administrative functionality for managing the metro ticketing system.

The manager can:

1. Authenticate using the Admin PIN.
2. Update ticket prices.
3. Change the operational status of metro lines.
4. Set a line to `Maintenance` to temporarily prevent new bookings.
5. Return a line to `Active` when it is operational again.

---

## Technologies

* **Python**
* **Command-Line Interface (CLI)**
* **Object-Oriented / Modular Programming**
* **File Handling**
* **Git & GitHub**
