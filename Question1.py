menu = {
    1: ("Chips", 2.50),
    2: ("Chocolate", 3.00),
    3: ("Cookies", 2.00),
    4: ("Soda", 1.50),
    5: ("Juice", 2.25),
    6: ("Water", 1.00)
}

selected_items = []
total_cost = 0


print("---- Snack and Drink Menu ----")
for number, item in menu.items():
    print(number, "-", item[0], ": $", item[1])

print("\nType the item number to select it.")
print("Type 'done' when you are finished.\n")


while True:
    choice = input("Choose an item number: ")

    if choice.lower() == "done":
        break

    if choice.isdigit():
        choice = int(choice)
        if choice in menu:
            item_name, price = menu[choice]
            selected_items.append((item_name, price))
            total_cost += price
            print(item_name, "added to your order.")
        else:
            print("Invalid item number.")
    else:
        print("Please enter a number or 'done'.")


print("\n------ Receipt ------")
for item, price in selected_items:
    print(item, "- $", price)

print("---------------------")
print("Total Cost: $", total_cost)