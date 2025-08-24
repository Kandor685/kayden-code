
total_items = 100


item_name = "Sony Playstation 5"

item_price = 418.99

in_stock = True


def print_inventory(total_items, item_name, item_price, in_stock,):
   
    print(f"Item: {item_name}")
    print(f"Cost: £{item_price}")
    TAX_RATE = 0.07
    print(f"Price including Tax: £{(item_price * TAX_RATE) + item_price}")
    if in_stock == True:
        print("Item is in stock")
    else:
        print("Item is not in stock")
    print(f"Total Items: {total_items}")
print_inventory(total_items, item_name, item_price, in_stock,)

#2 methods of f strings:
#(f"string"{variable})
#("String" + str(variable))