# main.py

from billing_manager import add_item, remove_item, view_bill, get_total

def menu(): #Defining the menu for billing 
    print("\n------ THE STORE BILLING SYSTEM ------")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Bill")
    print("4. View Total Amount")
    print("5. End")

while True:
    menu()
    choice = input("Enter Your Choice: ")

    # To Add items for billing
    if choice == "1":
        name = input("Enter Item Name: ")
        amount = input("Enter Price Of The Item: ")

        if amount.replace('.', '', 1).isdigit():
            amount = float(amount)
            add_item(name, amount)
            print("Item Has Been Added!")
        else:
            print("Invalid Price!, Please write correct price")

    # To remove an item from the bill
    elif choice == "2":
        name = input("Enter the name of the item you want to remove: ")
        if remove_item(name):
            print("Item has been successfully removed!")
        else:
            print("Item not found, Please write the correct item.")

    # To View the bill
    elif choice == "3":
        items = view_bill()
        if not items:
            print("No items found, Please add items to view the bill.")
        else:
            print("\n--- Your Bill is ---")
            for item, price in items:
                print(f"{item} : ₹{price}")

    # To View total amount 
    elif choice == "4":
        total = get_total()
        print(f"\nTotal Amount: ₹{total}")

    elif choice == "5":
        print("Thank you for using the Store Billing System!")
        break

    else:
        print("Invalid choice. Please Try again.")      