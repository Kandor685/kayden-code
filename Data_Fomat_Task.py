#Task 1- Create an Event registration system using CSV, JSON, or XML

#Data fields and how they'll be stored in the database

#Date of event- date
#email- string
#first name- string
#last name- string
#phone number- string
#date of birth- date 

import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path

email = input("Enter your email: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
phone_number = input("Enter your phone number: ")
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

#create a dataset
dataset = [
    {"id": 1, "date of event": "2025-06-10", "email": email, "first name": first_name, "last name": last_name, "phone number": phone_number, "date of birth": date_of_birth}
    
]

#create output folder
output_folder = Path("Regeistration_Info")
output_folder.mkdir(exist_ok=True)

# Convert to CSV
csv_file = output_folder / "dataset.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=dataset[0].keys())
    writer.writeheader()
    writer.writerows(dataset) 

# Convert to JSON
json_file = output_folder / "dataset.json"
with open(json_file, mode="w") as file:
    json.dump(dataset, file, indent=4)

# Convert to XML
xml_file = output_folder / "dataset.xml"
root = ET.Element("users")
user = ET.SubElement(root, "user")
for key, value in dataset[0].items():
    ET.SubElement(user, key).text = str(value)

tree = ET.ElementTree(root)
tree.write(xml_file)

print("Successfully Registered! Your information has been saved in", output_folder)