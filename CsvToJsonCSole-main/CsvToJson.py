import csv
import json
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class CsvToJsonConverter:
    def __init__(self, master):
        self.master = master
        master.title("CSV to JSON Converter")
        master.configure(bg="indigo")
        master.geometry("175x275")

        self.label = tk.Label(master, text="Select CSV file to convert:", bg="black", fg="white")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="s")

        self.button = tk.Button(master, text="Import CSV", command=self.import_csv, bg="steelblue", fg="white", width=20, height=3)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="n")

        self.convert_button = tk.Button(master, text="Convert to JSON", state="disabled", command=self.convert_to_json, bg="steelblue", fg="white", width=20, height=3)
        self.convert_button.grid(row=2, column=0, padx=10, pady=10, sticky="n")

        self.quit_button = tk.Button(master, text="Quit", command=master.quit, bg="steelblue", fg="white", width=20, height=3)
        self.quit_button.grid(row=3, column=0, padx=10, pady=10, sticky="n")

    def import_csv(self):
        csv_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if csv_file_path:
            self.csv_file_path = csv_file_path
            self.convert_button.config(state="normal")

    def convert_to_json(self):
        with open(self.csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            output = []
            obj = {} 
            obj["id"] = ""
            obj["name"] = "Test"
            obj["profiles"] = [] 
            for row in reader:
                profile = {}
                profile["id"] = row["profile_id"]
                profile["name"] = row["profile_name"]
                profile["email"] = row["email"]
                profile["phone"] = row["phone"]
                profile["billingDifferent"] = row["billing_different"]
                profile["card"] = {}
                profile["card"]["number"] = row["card_number"]
                profile["card"]["expMonth"] = row["card_expMonth"]
                profile["card"]["expYear"] = row["card_expYear"]
                profile["card"]["cvv"] = row["card_cvv"]
                profile["delivery"] = {}
                profile["delivery"]["firstName"] = row["delivery_firstName"]
                profile["delivery"]["lastName"] = row["delivery_lastName"]
                profile["delivery"]["address1"] = row["delivery_address1"]
                profile["delivery"]["address2"] = row["delivery_address2"]
                profile["delivery"]["city"] = row["delivery_city"]
                profile["delivery"]["zip"] = row["delivery_zip"]
                profile["delivery"]["country"] = row["delivery_country"]
                profile["delivery"]["state"] = row["delivery_state"]
                profile["billing"] = {}
                profile["billing"]["firstName"] = row["billing_firstName"]
                profile["billing"]["lastName"] = row["billing_lastName"]
                profile["billing"]["address1"] = row["billing_address1"]
                profile["billing"]["address2"] = row["billing_address2"]
                profile["billing"]["city"] = row["billing_city"]
                profile["billing"]["zip"] = row["billing_zip"]
                profile["billing"]["country"] = row["billing_country"]
                profile["billing"]["state"] = row["billing_state"]
                obj["profiles"].append(profile)
            output.append(obj)

        json_file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")], initialfile="billing.json")
        if json_file_path:
            with open(json_file_path, 'w') as outfile:
                json.dump(output, outfile, indent=2)
                messagebox.showinfo(title="Conversion Complete", message="CSV to JSON conversion successful!")

root = tk.Tk()
converter = CsvToJsonConverter(root)
root.mainloop()
