
import json
from datetime import datetime

stock_data = {}

def add_item(item, qty=0, logs=None):
    if not item:
        return
    current_qty = stock_data.get(item, 0)
    stock_data[item] = current_qty + qty
    if logs is not None:
        logs.append(f"Added {qty} of {item} at {datetime.now()}")

def remove_item(item, qty):
    
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Item not found, handle gracefully
        pass

def get_qty(item):
    
    return stock_data.get(item, 0)

def load_data(file):
    
    global stock_data
    with open(file, 'r', encoding='utf-8') as f:
        stock_data = json.load(f)

def save_data(file):
    
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(stock_data, f)

def print_data():
    
    for item, qty in stock_data.items():
        print(f"{item} - {qty}")

def check_low_items(threshold=5):
    
    result = []
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)
    return result

def main():
    logs = []
    add_item("apple", 10, logs)
    add_item("banana", -2, logs)
    add_item("123", 10, logs)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data("inventory.json")
    load_data("inventory.json")
    print_data()
    # Removed unsafe eval usage

if __name__ == "__main__":
    main()
