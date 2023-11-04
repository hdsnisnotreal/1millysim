# Initialize the budget
budget = 1000000

# Create an empty list to store your purchases
purchases = []

# Main simulation loop
while budget > 0:
    print(f"Your remaining budget: ${budget}")
    link = input("Enter a link to make a purchase (or 'done' to finish): ")

    if link.lower() == 'done':
        break

    try:
        price = float(input("Enter the price of the item: $"))
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        continue

    if price <= budget:
        budget -= price
        purchases.append((link, price))
        print(f"Purchase successful! You now have ${budget} left.")
    else:
        print("Insufficient budget for this purchase. Please choose a cheaper item or finish your shopping.")

# Display the final list of purchases
print("\nYour purchases:")
for i, (link, price) in enumerate(purchases, 1):
    print(f"{i}. Link: {link}, Price: ${price:.2f}")

print(f"Remaining budget: ${budget}")
print("Thank you for shopping!")
