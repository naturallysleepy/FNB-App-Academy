# Create a shopping cart program that will continuously ask the user for a product and its price.
# Must have an exit clause if user wishes to stop adding products to cart
# At the end, print out the items and the total price of all products in the cart 

# Initialize variables
total_price = 0.00

# Cart is a dictionary for storing products and their prices
cart = {}
item_no = 0  # Counter for the number of items in the cart

# Loop to obtain products and prices
while True:
    
    # Obtain valid product name
    while True:
        product = input("Enter a food product or 'exit' to finish: ").strip().lower()
        # Check if product is empty
        if product == "":
            print("Product name cannot be empty. Please try again.")
        else:
            break
    
    # Check if the user wants to exit
    if product == 'exit':
        break
    
    # Obtain valid price
    while True:
        try:
            price = float(input(f"Enter the price for {product}: R"))
            
            # If price is positive, exit loop
            if price >= 0:
                break
            else:
                # If price is not positive, prompt again
                print("Price must be a positive number. Please try again.")
        # Erroneous input check
        except ValueError:
            print("Invalid input. Please enter a valid price.")
    
    # Add product and price to the cart
    if product in cart:
        cart[product] += price
    else:
        cart[product] = price
    
    # Update total price
    total_price += price
    
    # Increment item number
    item_no += 1
    
    # Print confirmation message
    print(f"{product.title()} added to cart!\n" f"Current total: R{total_price}\n" f"There are {item_no} items in your cart.")
    
    
# Print final cart and total price

# Check if the cart is empty
if item_no == 0:
    print("Your cart is empty.")
# If the cart is not empty, print the items
else:
    print("\nYour shopping cart contains:")
    for item in cart:
        print(f"{item.title()}: R{cart[item]}")

# Print the total price
print(f"\nYour total is: R{total_price}")

# End of shopping cart program
    
    
    
    