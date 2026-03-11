
movies = {
    "1": {"title": "War Machine", "time": "6:00 PM", "price": 12},
    "2": {"title": "Spider-Man", "time": "8:00 PM", "price": 10},
    "3": {"title": "Iron Man", "time": "9:30 PM", "price": 11}
}

total_cost = 0
total_tickets = 0

while True:
    print("\nAvailable Movies:")
    for key, movie in movies.items():
        print(key + ".", movie["title"], "-", movie["time"], "- $", movie["price"])

    choice = input("Choose a movie (1-3): ")

    if choice in movies:
        tickets = int(input("How many tickets do you want? "))

        price = movies[choice]["price"]
        cost = price * tickets

        print("You selected:", movies[choice]["title"])
        print("Total price: $", cost)

        total_cost += cost
        total_tickets += tickets
    else:
        print("Invalid choice.")

    again = input("Do you want to book another movie? (yes/no): ").lower()

    if again == "no":
        break

print("\nBooking Summary")
print("Total tickets booked:", total_tickets)
print("Total cost: $", total_cost)