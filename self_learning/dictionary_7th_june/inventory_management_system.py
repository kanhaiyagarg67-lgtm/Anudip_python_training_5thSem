# program for inventory  management system
#enter the product name and stock in dictionary
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Display products with stock less than 10
print("Products with stock less than 10:")
for product, stock in inventory.items():
    if stock < 10:
        print(product, stock)

# Count products having stock more than 50
count = 0
for stock in inventory.values():
    if stock > 50:
        count += 1
print("Products with stock more than 50:", count)

# Find product with minimum stock
min_product = min(inventory, key=inventory.get)
print("Product with minimum stock:", min_product, inventory[min_product])

# Products requiring restocking
restock = []
for product, stock in inventory.items():
    if stock < 20:
        restock.append(product)
print("Products requiring restocking:", restock)

# Total inventory count
total = 0
for stock in inventory.values():
    total += stock
print("Total inventory count:", total)
