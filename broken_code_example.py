#menu items stored as a dictionary
menu = (                                                                                                             
    "Nachos": 5.50 , "Soup":4.95,
    "Burger":10.50, "Brisket": 12.50, "Ribs":15.00,
    "Corn":2.50, "Fries":3.00, "Salad":3.25
)

#checks if server name contains only letters
def get_server_name():
    flag = true                                                                                                      

    while flag:

        server_name = input('Please enter your name: ')

        if server_name.isalphanumeric() == False:
            print("Sorry you have not entered a recognised name.")
            flag = True

        else:
            server_name = "Server name: {}".format(server_name.capitalize())
            flag = False

    return server_name

#checks if table number is an integer
def get_table_num()
    flag= True

    while flag:
            
        table_num = input('Enter table number:  ')

        try:
            int(tabl_num)                                                                                            
            print("Sorry, you did not enter a table number")
            flag = True
        except:
            print("Sorry, you did not enter a table number")
            flag = True
        else:
            table_num = int(table_num)
            if table_num < 1 or table_num > 9:
                print("Table number must be between 1 and 10")
                flag = True
            else:
                flag = False

        return table_num

