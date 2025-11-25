# ATM Simulation Project Statement

---

# Problem Statement
The goal is to create a **functional and safe simulation of an ATM (Automated Teller Machine) system** to demonstrate fundamental programming concepts, including data structures (dictionaries for accounts), control flow (loops, conditionals), input validation, and basic function decomposition. The current account data is volatile (in-memory), necessitating robust logic to handle transactional updates and user input correctly.

---

# Scope of the Project
The scope of this project is strictly limited to a **command-line interface (CLI) application** in Python.

# Inclusions (In Scope)
* "Core Transaction Functions:" :- Balance check, deposit, and withdrawal.
* "Security Features:" :-  Account number/PIN verification and a limit of 3 failed login attempts.
* "Account Management:" :- The ability to reset the user's PIN.
* "Input Validation:" :- Handling non-numeric input for transaction amounts.
* "Business Logic:" :- Enforcing a maximum single-transaction withdrawal limit of **$1000** and checking for insufficient funds.

# Exclusions (Out of Scope)
* "Data Persistence:" :- The account data is hard-coded into a Python dictionary (`ACCOUNTS`). The project **does not** include connecting to a database (e.g., SQLite, PostgreSQL) or saving data to an external file (e.g., CSV, JSON). All changes are lost when the program closes.
* "External Integration:" :- No integration with real banking systems, APIs, or external services.
* "User Interface (UI):" :- No graphical user interface (GUI) or web interface.
* "Transfer Functions:" :- Account-to-account transfers are not included.
* "Advanced Security:" :- No encryption, logging, or multi-factor authentication.

---

# Target Users
The primary target users for this project are:

* "Beginning Python Developers:" :- Individuals learning Python who need a practical, real-world example of how to combine dictionaries, functions, and control structures to create a useful application.
* "Interviewers/Educators:" :- Those assessing a candidate's or student's ability to implement simple, clean, and functional object-oriented/procedural logic.
* "Casual Users:" :- Anyone who wants to quickly test and interact with a simulated bank account environment via the command line.

---

# High-Level Features

| Feature Category | High-Level Feature Description |
| 
| "Authentication & Security" :- Securely log in using account number and 4-digit PIN with a fixed limit on failed attempts. 
| "Enquiry" :-  Display the user's current account balance in a clear, formatted currency view. 
| "Deposit Transaction" :-  Add funds to the account, ensuring the deposit amount is a positive number. 
| "Withdrawal Transaction" :- Subtract funds, enforcing checks for insufficient balance and a $1000 transaction limit.
| "Account Update" :- Allow the user to change their 4-digit PIN after successful login. 
