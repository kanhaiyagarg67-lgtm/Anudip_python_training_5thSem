'''1. Online Shopping Order Analytics 
Problem Statement 
An e-commerce company stores product sales data as: 
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products sold more than 20 times.  
2. Find the best-selling product.  
3. Find the least-selling product.  
4. Calculate total products sold.  
5. Create a list of products requiring promotion (sales < 15).  
6. Count products having sales between 10 and 30.  '''


#sales data for 10 products
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}
#Task 1: Display products sold more than 20 times.
print("Products Sold More Than 20 Times:")  
for product, quantity in sales.items():
    if quantity>20:
        print(product)
print("---------------------------------")
#Task 2: Find the best-selling product.
dict_items = list(sales.items())
best_seller = dict_items[0][0]
best_sales = dict_items[0][1]
for item in dict_items:
    if item[1] > best_sales:
        best_seller = item[0]
        best_sales = item[1]
print("Best Selling Product:", best_seller, "(", best_sales, ")")
print("---------------------------------")      
#Task 3: Find the least-selling product.
least_seller = dict_items[0][0]
least_sales = dict_items[0][1]
for item in dict_items:
    if item[1] < least_sales:
        least_seller = item[0]
        least_sales = item[1]
print("Least Selling Product:", least_seller, "(", least_sales, ")")
print("---------------------------------")      
#Task 4: Calculate total products sold.
total_sold = 0
for quantity in sales.values():
    total_sold += quantity
print("Total Units Sold:", total_sold)
print("---------------------------------")      

''' Sample Output 
Products Sold More Than 20 Times: 
Mouse 
Keyboard 
Headphones 
Router 
 
Best Selling Product: Mouse (45) 
 
Least Selling Product: Printer (8) 
 
Total Units Sold: 213 
 
Products Requiring Promotion: 
['Monitor', 'Printer', 'Tablet'] 
 
Products Having Sales Between 10 and 30: 6'''
