```markdown
# Riyadh Metro Ticketing & Route Management CLI

## Overview
An interactive command-line ticketing and route management system for the Riyadh Metro network[cite: 1, 4]. The system serves two primary roles: **Passengers** who can browse lines, check operational status, view routes, calculate fares with student discounts, and checkout with exported invoices; and **Station Managers** who can manage ticket pricing tariffs and toggle line maintenance status to suspend or resume bookings[cite: 1, 2, 3, 4, 5].

---

## Features & User Stories

### As a Passenger, I should be able to:
* Browse all available Riyadh Metro lines, terminal stations, and their current operational status (`Active` or `Maintenance`)[cite: 1, 4].
* View detailed route descriptions for any specific line (1 to 6)[cite: 1, 4].
* Select an active line, duration (daily, monthly, yearly), and travel class (economy, first class) to view ticket prices[cite: 1, 4].
* Apply an eligible university student discount (50% OFF) by verifying university selection and student ID format[cite: 1, 3].
* Add configured tickets to a personal shopping cart[cite: 1].
* View items in the cart along with the calculated total amount[cite: 1].
* Proceed to checkout, confirm the passenger name, and automatically export an official text invoice (`Invoice_PassengerName_timestamp.txt`)[cite: 1, 2].

### As a Manager, I should be able to:
* Authenticate securely using an Admin PIN code (`4123`)[cite: 1].
* Update ticket pricing dynamically across durations and tiers within the authorized range (4 to 5000 SAR)[cite: 5].
* Toggle a metro line's operational status between `Active` and `Maintenance` to suspend ticket booking during track service[cite: 4].

---

## Project Structure

```text
Riyadh_Metro_Project/
├── main.py                          # Application entry point and interactive CLI menu
├── Metro_admin_section/             # Core business logic package
│   ├── __init__.py
│   ├── Metro_Data.py                # Line routes, station statuses, and pricing structures
│   ├── Adminstrative.py             # Administrative controls (pricing updates & status toggling)
│   ├── Student_Discount.py          # Academic verification and discount processing
│   └── Invoice.py                   # Automated file-based receipt generator
├── requirements.txt                 # Project environment dependencies
└── README.md                        # Documentation and project guide

```

---

## Usage

### 1. Run the Project

Make sure you are in the project root directory, then run:

```bash
python main.py

```

### 2. Interactive Navigation

The application runs as an interactive menu-driven interface:

* Enter your passenger name when prompted to personalize your session.


* Type `1` to browse all lines, their full route descriptions, and active/maintenance statuses.


* Type `2` to inspect a specific line by number (1-6).


* Type `3` to configure and purchase a ticket (checks line status, prompts for duration, class, and optional student verification).


* Type `4` to review your cart summary and complete checkout with an exported invoice file.


* Type `5` to enter Manager Mode (requires PIN: `4123`) to update tariffs or toggle maintenance mode.


* Type `6` to exit the CLI.


```
