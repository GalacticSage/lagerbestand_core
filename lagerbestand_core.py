import json
import pandas as pd
from datetime import datetime

# Function to read JSON data from a file
def read_json(lager_json):
    with open(lager_json, "r") as json_file:
        data = json.load(json_file)
    return data

# Function to write JSON data to a file
def write_json(data, lager_json):
    with open(lager_json, "w") as json_file:
        json.dump(data, json_file, indent=4)

# Function to format data for display
def formatted_data(data):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    formatted_data = dt_string + "\n"
    for key, value in data.items():
        formatted_key = key.replace("_", " ").replace("-", " ").title()
        formatted_data += f"{formatted_key}: {value}\n"
    return formatted_data

# Function to export data to an Excel file
def export_to_excel(data, filePath):
    # Construct a list of dictionaries with the desired structure
    data_list = [{"Item": key, "Quantity": value} for key, value in data.items()]

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)

    df.to_excel(filePath, index=False)

# Function to increase the quantity of an item
def increase_quantity(lager_json, data, item_name, quantity_to_increase):
    # Check if the item exists in the data dictionary
    if item_name in data:
        # Increase the quantity (as string concatenation)
        current_quantity = data[item_name]
        new_quantity = str(int(current_quantity) + quantity_to_increase)
        data[item_name] = new_quantity
        # Save the updated data to the JSON file
        write_json(data, lager_json)
    else:
        print(f"Item '{item_name}' not found in the inventory.")

# Function to decrease the quantity of an item
def decrease_quantity(lager_json, data, item_name, quantity_to_decrease):
    # Check if the item exists in the data dictionary
    if item_name in data:
        # Decrease the quantity (as string concatenation)
        current_quantity = data[item_name]
        new_quantity = str(max(0, int(current_quantity) - quantity_to_decrease))
        data[item_name] = new_quantity
        # Save the updated data to the JSON file
        write_json(data, lager_json)
    else:
        print(f"Item '{item_name}' not found in the inventory.")

# Function to remove an item from the inventory
def remove_item(lager_json, data, item_name):
    # Check if the item exists in the data dictionary
    if item_name in data:
        del data[item_name]
        # Save the updated data to the JSON file
        write_json(data, lager_json)
        print(f"Item '{item_name}' has been removed from the inventory.")
    else:
        print(f"Item '{item_name}' not found in the inventory.")

# Function to add an item to the inventory
def add_item(lager_json, data, item_name, quantity):
    # Check if the item already exists in the data dictionary
    if item_name in data:
        current_quantity = data[item_name]
        new_quantity = str(int(current_quantity) + quantity)
        data[item_name] = new_quantity
    else:
        data[item_name] = str(quantity)
    
    # Save the updated data to the JSON file
    write_json(data, lager_json)
    print(f"Added {quantity} of '{item_name}' to the inventory.")