import pandas as pd

#Displays the main menu and allows user to select option

def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show total sales for all items (Between Specific Dates)")
        print("3. Exit")

        main_menu_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Shop selection from user
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a product from the list:")
        print("Please enter the number of the product (1-8)")
        print("1.  T-Shirt")
        print("2.  Keyring")
        print("3.  Mug")
        print("4.  Cap")
        print("5.  Toy")
        print("6.  Poster")
        print("7.  Magnet")
        print("8.  Pen")
        print("######################################################")

        shop_list = ["T-Shirt","Keyring","Mug", "Cap","Toy","Poster", "Magnet", "Pen"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = shop_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date

#imports data set and extracts data and returns data for a specific item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv") 
    df2 = df1.loc[df1['Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    return df3


def total_items_sold(startdate, enddate):
    #read the csv file
    df1 = pd.read_csv("Task4a_data.csv") 
    #calculate totals
    total = df1.groupby(['Item']).sum()
    #4. Get total sales of all items between selected dates
    total_out = total.loc[:, startdate:enddate].sum(axis=1, numeric_only = True)
    return total_out

while True:
    main_menu = menu()

    #menu choice 1 total sales for selected product
    if main_menu == 1:

        #get user input
        item = get_product_choice()
        start_date = get_start_date()
        end_date = get_end_date()
    
        #extract requested data
        extracted_data = get_selected_item(start_date, end_date)

        #display requested data
        print("\n")
        print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
        extract_no_index = extracted_data.to_string(index=False)

        print(extract_no_index)
        print("\n")
    #Option 2 Show all sales data
    elif main_menu == 2:
        
        start_date = get_start_date()
        end_date = get_end_date()
        extracted_data = total_items_sold(start_date, end_date)
        
        #print the information
        print("\nThe total sales between {} and {} were: ".format(start_date, end_date))
        print(extracted_data)
        
    else:
        print("Thank you for using the dashboard")
        exit()
