import csv

# with open('data.csv', 'w', newline = '') as file:
#     write = csv.writer(file)
#     write.writerow(["Name", "Age", "City"])
#     write.writerow(["Allice", 30, "New York"])
    
# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

with open("demo.csv", 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    
with open("demo.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
try:
    with open('nonexistantfile.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("ERROR: File Not Found!")