#program for inventory stock alert system
# List of stock quantities
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# Variable to count out of stock products
out_of_stock = 0

# Empty list to store products that need restocking
restock_required = []

# Variable to count available products
available_products = 0

# Empty list to store products with stock >= 15
healthy_stock = []

# Loop through each quantity in stock list
for quantity in stock:

    # If quantity is 0, product is out of stock
    if quantity == 0:
        out_of_stock = out_of_stock + 1

    # If quantity is less than 10, restocking is required
    if quantity < 10:
        restock_required.append(quantity)

    # If quantity is greater than 0, product is available
    if quantity > 0:
        available_products = available_products + 1

    # If quantity is 15 or more, stock is healthy
    if quantity >= 15:
        healthy_stock.append(quantity)

# Display all results
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)
