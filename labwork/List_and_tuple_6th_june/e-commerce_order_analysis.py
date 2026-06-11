'''An online store records orders as: 
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 
Write a program to: 
• Display all products costing more than ₹1000.  
• Find the most expensive product.  
• Calculate the total order value.  
• Count products costing below ₹1000. '''

#create orders records

orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 


#To Display all products costing more than ₹1000.
print("Product costing more than rs. 1000")
for order in orders:
    if(order[1]>1000):
        print(order[0])

# To Find the most expensive product.
max_price=0
for record in orders:
    if record[1]>max_price:
        max_price=record[1]
        product=record[0]
print("Most Expensive Product : ",product,max_price)

#Task -3 To Calculate the total order value.
total=0
for order in orders:
    total+=order[1]
print("total order value:")
print(total)


#Task -4 To Count products costing below ₹1000.
count=0
for order in orders:
    if(order[1]<1000):
        count+=1
print("Products costing below 1000")
print(count)
