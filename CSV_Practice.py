#Import data
#create Menu
#Read data as required
#output the data

import pandas as pd 

df = pd.read_csv("vgsales.csv")

def view_all_records():
    #Display all the records
    print(df.to_string(index=False))

def search_record():
    #Search for a record on a specific field
    column = input(f"Enter the column name to search by ({', '.join(df.columns)}): ")
    if column not in df.columns:
        print("Error: Invalid column name!")
        return
    value = input("Enter the value to search for: ") 
    value = df[df[column].astype(str).str.contains(value, case = False, na = False)]
    print(value if not value.empty else "No results found.")
    
def search_by_year(df):
    #Search for a year
    df = df.dropna(subset=["Year"])
    df["Year"] = df["Year"].astype(int)
    year = int(input("Choose a year: "))
    if year not in df["Year"].values:
        print("Error: Invalid year!")
        return
    year_results = df[df["Year"] == year]
    print(df["Year"])
    print(year_results[["Year", "Rank", "Name"]].head(30) if not year_results.empty else "No results found.")
def main():
    while True:
        print("\nGame Data Display")
        print("#####################")
        print("1. View All Records")
        print("2. Search for a Record")
        print("3. Search by Year")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            view_all_records()
        elif choice == "2":
            search_record()
        elif choice == "3":
            search_by_year(df)
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
main()