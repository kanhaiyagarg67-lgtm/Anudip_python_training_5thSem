'''Problem 5: Online Shopping Cart Analyzer 
Problem Statement 
The prices of products added to a shopping cart are stored below. 
Sample Data 
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 
1. Calculate the total cart value.  
2. Find the most expensive and cheapest products.  
3. Count products eligible for premium shipping (price > ₹1000).  
4. Generate a discount list (products above ₹1500).  
5. Calculate the average product price.  '''


# entering the prices in cart
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

total = sum(cart)  #Calculate the total cart value. 
maximum = max(cart) # Find the most expensive products.  
minimum = min(cart)  #Find the most cheapest products.
average = total / len(cart)  #Calculate the average product price.  

premium_count = 0  #Count products eligible for premium shipping (price > ₹1000). 
discount_list = []  #Generate a discount list (products above ₹1500).  

for price in cart:
    if price > 1000:
        premium_count += 1

    if price > 1500:
        discount_list.append(price)

print("Total Cart Value: ₹", total)
print("Most Expensive Product: ₹", maximum)
print("Cheapest Product: ₹", minimum)
print("Premium Shipping Eligible Products:", premium_count)

print("Discount Eligible Products:")
print(discount_list)

print("Average Product Price: ₹", average)

'''
Sample Output 
Total Cart Value: ₹11,097 
 
Most Expensive Product: ₹2,500 
 
Cheapest Product: ₹300 
 
Premium Shipping Eligible Products: 4 
 
Discount Eligible Products: 
[2500, 1800] 
 
Average Product Price: ₹1,109.7'''
