import json
import pandas as pd
import openpyxl
import tkinter
from tkinter import filedialog
from datetime import datetime

def read_json(lager_json):
        with open(lager_json, "r") as json_file:
            data = json.load(json_file)
            json_file.close()
        return data

def formatted_data(data):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        formatted_data = dt_string + "\n"
        for key, value in data.items():
            formatted_key = key.replace("_", " ").replace("-", " ").title()
            formatted_data += f"{formatted_key}: {value}\n"
        return formatted_data

def export_to_excel(data):
        # Construct a list of dictionaries with the desired structure
        data_list = [{"Item": key, "Quantity": value} for key, value in data.items()]

        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(data_list)

        # Use file dialog to get the output path
        tkinter.Tk().withdraw()  # Prevents an empty tkinter window from appearing
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])

        # If the user didn't cancel the file dialog, save the DataFrame to Excel
        if file_path:
            df.to_excel(file_path, index=False)