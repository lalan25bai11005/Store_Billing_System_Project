# Problem Statement: Simple Store Billing System Automation:

In many small stores, billing is still performed manually using calculators or handwritten notes. This is time-consuming and error-prone , especially when items need to be removed or edited.

The goal of this project is to create a simple menu-driven program that automates basic billing operations and calculates the total amount accurately. This console application is designed to help a small shopkeeper manage billing operations efficiently.


# Scope and Functional Requirements: 

The system provides the following core functions:


=> Add Item - The user can enter an item name and its price to add it to the current bill.


=> Remove Item - The user can remove a specific item by entering its name.


=> View Bill - Display all items currently added along with their individual prices.


=> View Total Amount - Calculate and display the total amount of the bill.


=> End - Exit the program gracefully.

# Non-Functional Requirements:


=> Usability - The menu options should be easy to understand for any user.


=> Accuracy - Item prices and the total amount must be calculated correctly.


=> Maintainability - Core billing logic is kept in a separate module (billing_manager.py) to keep the code organized.


=> Error Handling - The program validates price input (allowing digits and a single decimal point) and handles invalid menu choices with clear messages.


# Technologies Used:

The project is implemented in Python  using Functions, Lists, and a Modular Code structure.