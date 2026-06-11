''' E-Commerce Inventory & Sales Dashboard 
Problem Statement 
An online store wants to manage products and sales. 
Example Structure 
products = { 
    "P101": { 
        "name": "Laptop", 
        "price": 55000, 
        "stock": 12, 
        "sold": 25 
    } 
} 
Maintain records of at least 30 products. 
Requirements 
1. Display all products.  
2. Add a new product.  
3. Update stock after sales.  
4. Find out-of-stock products.  
5. Find products with stock less than 5.  
6. Calculate total inventory value.  
7. Find best-selling product.  
8. Find least-selling product.  
9. Calculate total revenue generated.  
10. Generate a low-stock report.  
11. Display products whose sales exceed the average sales.  
12. Create a dictionary of products eligible for promotion (sales < 10).  
Challenge 
Generate a complete business report.'''


# E-Commerce Inventory & Sales Dashboard

# Store details of 30 products in nested dictionary
products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Mouse", "price": 800, "stock": 45, "sold": 60},
    "P103": {"name": "Keyboard", "price": 1800, "stock": 20, "sold": 35},
    "P104": {"name": "Monitor", "price": 12000, "stock": 8, "sold": 18},
    "P105": {"name": "Printer", "price": 9000, "stock": 0, "sold": 7},
    "P106": {"name": "Tablet", "price": 28000, "stock": 10, "sold": 22},
    "P107": {"name": "Speaker", "price": 3500, "stock": 4, "sold": 12},
    "P108": {"name": "Webcam", "price": 2500, "stock": 15, "sold": 28},
    "P109": {"name": "Headphones", "price": 4200, "stock": 6, "sold": 30},
    "P110": {"name": "Router", "price": 3200, "stock": 3, "sold": 9},

    "P111": {"name": "Mobile", "price": 25000, "stock": 18, "sold": 40},
    "P112": {"name": "Charger", "price": 1200, "stock": 50, "sold": 75},
    "P113": {"name": "Power Bank", "price": 2200, "stock": 25, "sold": 32},
    "P114": {"name": "Smart Watch", "price": 5000, "stock": 7, "sold": 20},
    "P115": {"name": "Earbuds", "price": 3000, "stock": 30, "sold": 55},
    "P116": {"name": "USB Cable", "price": 300, "stock": 80, "sold": 90},
    "P117": {"name": "Hard Disk", "price": 4500, "stock": 9, "sold": 14},
    "P118": {"name": "SSD", "price": 6000, "stock": 11, "sold": 26},
    "P119": {"name": "RAM", "price": 3500, "stock": 5, "sold": 16},
    "P120": {"name": "Graphics Card", "price": 45000, "stock": 2, "sold": 6},

    "P121": {"name": "CPU", "price": 18000, "stock": 4, "sold": 11},
    "P122": {"name": "Motherboard", "price": 10000, "stock": 6, "sold": 13},
    "P123": {"name": "Cabinet", "price": 4000, "stock": 10, "sold": 8},
    "P124": {"name": "Cooling Fan", "price": 700, "stock": 35, "sold": 45},
    "P125": {"name": "Microphone", "price": 2500, "stock": 14, "sold": 19},
    "P126": {"name": "Tripod", "price": 1500, "stock": 16, "sold": 21},
    "P127": {"name": "Projector", "price": 35000, "stock": 1, "sold": 5},
    "P128": {"name": "Scanner", "price": 7500, "stock": 0, "sold": 4},
    "P129": {"name": "Pen Drive", "price": 600, "stock": 60, "sold": 85},
    "P130": {"name": "Memory Card", "price": 900, "stock": 40, "sold": 70}
}


# 1. Display all products
print("All Products:")

for pid, details in products.items():
    print(pid, "->", details["name"], details["price"], details["stock"], details["sold"])


# 2. Add a new product
new_id = input("\nEnter new Product ID: ")
new_name = input("Enter product name: ")
new_price = int(input("Enter product price: "))
new_stock = int(input("Enter product stock: "))
new_sold = int(input("Enter sold quantity: "))

products[new_id] = {
    "name": new_name,
    "price": new_price,
    "stock": new_stock,
    "sold": new_sold
}

print("New product added successfully")


# 3. Update stock after sales
update_id = input("\nEnter Product ID to update stock after sale: ")

if update_id in products:
    sold_now = int(input("Enter quantity sold now: "))

    # Check if enough stock is available
    if sold_now <= products[update_id]["stock"]:
        products[update_id]["stock"] = products[update_id]["stock"] - sold_now
        products[update_id]["sold"] = products[update_id]["sold"] + sold_now

        print("Stock updated successfully")
    else:
        print("Not enough stock available")
else:
    print("Product ID not found")


# 4. Find out-of-stock products
print("\nOut-of-Stock Products:")

for pid, details in products.items():
    if details["stock"] == 0:
        print(pid, details["name"])


# 5. Find products with stock less than 5
print("\nProducts With Stock Less Than 5:")

for pid, details in products.items():
    if details["stock"] < 5:
        print(pid, details["name"], "Stock:", details["stock"])


# 6. Calculate total inventory value
# Inventory value = price * stock
total_inventory_value = 0

for details in products.values():
    total_inventory_value = total_inventory_value + (details["price"] * details["stock"])

print("\nTotal Inventory Value:", total_inventory_value)


# 7. Find best-selling product
product_items = list(products.items())

best_id = product_items[0][0]
best_sold = product_items[0][1]["sold"]

for pid, details in products.items():
    if details["sold"] > best_sold:
        best_id = pid
        best_sold = details["sold"]

print("\nBest-Selling Product:")
print(best_id, products[best_id]["name"], "Sold:", best_sold)


# 8. Find least-selling product
least_id = product_items[0][0]
least_sold = product_items[0][1]["sold"]

for pid, details in products.items():
    if details["sold"] < least_sold:
        least_id = pid
        least_sold = details["sold"]

print("\nLeast-Selling Product:")
print(least_id, products[least_id]["name"], "Sold:", least_sold)


# 9. Calculate total revenue generated
# Revenue = price * sold
total_revenue = 0

for details in products.values():
    total_revenue = total_revenue + (details["price"] * details["sold"])

print("\nTotal Revenue Generated:", total_revenue)


# 10. Generate a low-stock report
print("\nLow-Stock Report:")

for pid, details in products.items():
    if details["stock"] < 5:
        print(pid, details["name"], "Stock:", details["stock"])


# 11. Display products whose sales exceed the average sales
total_sales = 0

for details in products.values():
    total_sales = total_sales + details["sold"]

average_sales = total_sales / len(products)

print("\nAverage Sales:", average_sales)

print("\nProducts Whose Sales Exceed Average Sales:")

for pid, details in products.items():
    if details["sold"] > average_sales:
        print(pid, details["name"], "Sold:", details["sold"])


# 12. Create dictionary of products eligible for promotion
# Products with sales less than 10 are eligible for promotion
promotion_products = {}

for pid, details in products.items():
    if details["sold"] < 10:
        promotion_products[pid] = details

print("\nProducts Eligible For Promotion:")

for pid, details in promotion_products.items():
    print(pid, details["name"], "Sold:", details["sold"])


# Challenge: Complete business report
print("\n========== COMPLETE BUSINESS REPORT ==========")

print("Total Products:", len(products))
print("Total Inventory Value:", total_inventory_value)
print("Total Revenue Generated:", total_revenue)
print("Best-Selling Product:", products[best_id]["name"])
print("Least-Selling Product:", products[least_id]["name"])
print("Average Sales:", average_sales)
print("Promotion Products Count:", len(promotion_products))

print("=============================================")
