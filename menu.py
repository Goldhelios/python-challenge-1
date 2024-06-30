# Menu dictionary
from math import prod

menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
orderList = []
continueordering = True

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous

place_order = True
while place_order:
    print("From which menu would you like to order? ")

    i = 1
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    if menu_category.isdigit():

        if int(menu_category) in menu_items.keys():

            menu_category_name = menu_items[int(menu_category)]

            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            
            # 2. Ask customer to input menu clnitem number
            menu_items_number = input("What item number do you wish to order?: ")
            
            # 3. Check if the customer typed a number
            if menu_items_number.isdigit():
                # Convert the menu selection to an integer
                menu_items_number = int(menu_items_number)

                # 4. Check if the menu selection is in the menu items
                if menu_items_number in menu_items.keys():
                    # Store the item name as a variable
                    menu_item_name = menu_items[menu_items_number]["Item name"]

                    # Ask the customer for the quantity of the menu item
                    menu_item_quantity = input("how many do you want?: ")
                    
                    # Check if the quantity is a number, default to 1 if not
                    if menu_item_quantity.isdigit():
                        menu_item_quantity = int(menu_item_quantity)
                    else:
                        menu_item_quantity = 1

                    # Add the item name, price, and quantity to the order list
                    orderList.append({"Menu Item" : menu_item_name,
                                           "Item Price": menu_items[menu_items_number]["Price"],
                                           "Item Quantity" : menu_item_quantity})
                
                # Tell the customer that their input isn't valid
                else: 
                    print("Invalid Order")

                # Tell the customer they didn't select a menu option
            else:
                print(f"{menu_category} was not a menu option.")

    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    continueordering = True

    while continueordering == True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        if keep_ordering.upper() == "Y":

                # Keep ordering
                continueordering = False
                place_order = True

                # Complete the order
                print("Great, what else would you like to order?")
                # Since the customer decided to stop ordering, thank them for their order
        elif keep_ordering.upper() == "N":
            place_order = False
            continueordering = False
            print("Thank you for your order.")
            break
                # Exit the keep ordering question loop
        else:
            print("Try again.")
                # Tell the customer to try again


# Print out the customer's order
print("""
      Please find your reciept below for your order.
      """)

# Uncomment the following line to check the structure of the order
# print(orderList)
# print(orderList[0]["Menu Item"])
print(f"RECIEPT")
print("Item name                 | Price  | Quantity | Item Total")
print("--------------------------|--------|----------|-----------")
n=0
i=1
# # 6. Loop through the items in the customer's order
for orders in orderList:

    # 7. Store the dictionary items as variables
    orderItem = orderList[n]["Menu Item"]
    orderItemPrice = orderList[n]["Item Price"]
    orderItemQuantity = orderList[n]["Item Quantity"]
    orderItemTotal = orderItemQuantity * orderItemPrice
    n = n+1
    # 8. Calculate the number of spaces for formatted printing
    namegapspace = " " * (22 - len(orderItem))
    pricegapespace = " " *(5 - len(str(orderItemPrice)))
    quantityspace = " " * (8 - len(str(orderItemQuantity)))
    totalspace = " " *(8 - len(str(orderItemTotal)))

    # 9. Create space strings
    print(f"{i}. {orderItem}{namegapspace} | ${orderItemPrice:,.2F}{pricegapespace} | {orderItemQuantity}{quantityspace} | ${orderItemTotal:,.2F}{totalspace}")
    i = i+1

print("\n")
# 11. Calculate the cost of the order using list comprehension 
grandTotal = sum(order["Item Price"] * order["Item Quantity"] for order in orderList)
print(f"Total cost of the order: ${grandTotal:.2f}")


# grandTotal = (orderItemQuantity[i]*orderItemPrice[i] for i in range(len(str(orderItemQuantity))))

# print(grandTotal)



# Multiply the price by quantity for each item in the order list, then sum()
# and print the price
