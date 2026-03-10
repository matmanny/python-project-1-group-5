# Predefined grocery dictionary with prices
groceries = {
    "apple": 1.5,
    "banana": 0.8,
    "milk": 2.5,
    "bread": 2.0,
    "eggs": 3.0
}

cart = {}

print("Available groceries and prices:")
for item, price in groceries.items():
    print(item, "- $", price)

print("\nType the item name to add it to your cart.")
print("Type 'checkout' to finish.\n")

while True:
    item = input("Enter item name: ").lower()

    if item == "checkout":
        break

    if item in groceries:
        quantity = int(input("Enter quantity: "))
        
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity

        print(item, "added to cart.\n")
    else:
        print("Item not available.\n")

# Print final bill
print("\n------ Final Bill ------")
total = 0

for item, quantity in cart.items():
    price = groceries[item]
    subtotal = price * quantity
    total += subtotal
    print(item, "| Quantity:", quantity, "| Subtotal: $", subtotal)

print("-----------------------")
print("Total: $", total)