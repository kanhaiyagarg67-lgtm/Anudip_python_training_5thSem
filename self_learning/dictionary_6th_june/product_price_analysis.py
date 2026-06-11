#program for product price analysis
#enter the product with their price in dictionary
prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# Display products costing more than 5000
print("Products costing more than ₹5000:")
for product, price in prices.items():
    if price > 5000:
        print(product, price)

# Count products costing less than 3000
count = 0
for price in prices.values():
    if price < 3000:
        count += 1
print("Products costing less than ₹3000:", count)

# Find most expensive product
expensive = max(prices, key=prices.get)
print("Most expensive product:", expensive, prices[expensive])

# Products priced between 2000 and 10000
between = []
for product, price in prices.items():
    if price >= 2000 and price <= 10000:
        between.append(product)
print("Products priced between ₹2000 and ₹10000:", between)

# Total value of all products
total = 0
for price in prices.values():
    total += price
print("Total value of all products:", total)
