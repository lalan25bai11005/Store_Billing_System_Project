# billing_manager.py

items = []

def add_item(name, price):
    items.append((name, price))

def remove_item(name):
    for item in items:
        if item[0].lower() == name.lower():
            items.remove(item)
            return True
    return False

def view_bill():
    return items

def get_total():
    return sum(price for _, price in items)