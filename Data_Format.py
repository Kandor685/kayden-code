import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path

#create a dataset

dataset = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 25},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 35}

]

# create output folder
output_folder = Path("Data_Formats")
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

#Convert to XML
root = ET.Element("users")
for record in dataset:
    user = ET.SubElement(root, "user")
    for key, value in record.items():
        child = ET.SubElement(user, key)
        child.text = str(value)

xml_file = output_folder / "dataset.xml"
tree = ET.ElementTree(root)
tree.write(xml_file, encoding="utf-8", xml_declaration=True)

print(f"Files saved in {output_folder}")