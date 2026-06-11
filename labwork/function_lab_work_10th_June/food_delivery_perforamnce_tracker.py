'''Problem Statement 
Delivery times (in minutes) for different orders are given below: 
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Requirements 
Create the following functions: 
1. fastest_delivery(times) 
Returns the shortest delivery time. 
2. delayed_orders(times) 
Returns a list of orders taking more than 45 minutes. 
3. average_delivery_time(times) 
Returns the average delivery time. 
4. delivery_category(times) 
Displays order categories: 
• Fast → ≤ 30 minutes  
• Normal → 31–45 minutes  
• Delayed → > 45 minutes '''
'''
Problem Statement:
Delivery times (in minutes) for different orders are given below.
'''

# List containing delivery times of all orders
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]


# Function to find the shortest (fastest) delivery time
def fastest_delivery(times):
    return min(times)


# Function to return all delayed orders
# (orders taking more than 45 minutes)
def delayed_orders(times):
    order = []

    # Traverse each delivery time
    for time in times:
        if time > 45:
            order.append(time)

    return order


# Function to calculate average delivery time
def average_delivery_time(times):

    # Sum of all delivery times divided by total number of orders
    return sum(times) / len(times)


'''
Function to display order categories

Fast    -> <= 30 minutes
Normal  -> 31 to 45 minutes
Delayed -> > 45 minutes
'''
def delivery_category(times):

    # Traverse each delivery time
    for time in times:

        # Fast delivery
        if time <= 30:
            print(time, "-> Fast")

        # Normal delivery
        elif time <= 45:
            print(time, "-> Normal")

        # Delayed delivery
        else:
            print(time, "-> Delayed")


# Display fastest delivery time
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")

# Display delayed orders
print("\nDelayed Orders:")
print(delayed_orders(delivery_time))

# Display average delivery time
print("\nAverage Delivery Time:")
print(average_delivery_time(delivery_time), "minutes")

# Display category of each order
print("\nCategories:")
delivery_category(delivery_time)
'''Fastest Delivery: 18 minutes 
 
Delayed Orders: 
[60, 80, 55] 
 
Average Delivery Time: 
40.8 minutes 
 
Categories: 
28 -> Fast 
45 -> Normal 
60 -> Delayed'''
