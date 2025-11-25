# Simple Billing System for a Store:

A beginner-friendly Python billing system project where users can add items, remove items, view the bill, and view the total amount. This console application automates basic billing and ensures accurate calculations.

# Features:

The system provides a menu-driven interface with five options:


1. Add Item: Enter the item name and price to add it to the bill.

2. Remove Item: Remove an item from the bill by entering its name.

3. View Bill: Display the currently added items and their prices.

4. View Total Amount: Calculate and display the total cost of all the items combined.

5. End: Exit the application.

# System Architecture:

The project follows a clean, modular code design:


- main.py: Handles the User Interface (UI) and Menu display. It reads the user's choice and performs the corresponding action.



- billing_manager.py: Contains the Core Logic. It manages the internal bill data (list) and performs operations like adding, removing, and calculating the total.


# How to Run:

1. Save both files: main.py and billing_manager.py in the same directory.

2. Run the application from your console or terminal:

python main.py

# Future Enhancements:

The system can be improved with the following enhancements:

1. Add support for item quantities instead of assuming quantity 1 for every item.

2. Introduce discount and tax calculations (for example, GST).

3. Allow saving and loading bills from files so that records can be stored.

4. Enhance the user interface by adding colors or migrating to a graphical interface