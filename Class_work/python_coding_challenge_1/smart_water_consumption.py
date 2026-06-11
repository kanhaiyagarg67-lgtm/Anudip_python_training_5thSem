'''Problem 8: Smart Water Consumption Monitoring System 
Problem Statement 
Monthly water consumption (in litres) of households is recorded below. 
Sample Data 
water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
} 
Tasks 
1. Display houses consuming more than 3000 litres.  
2. Find the highest and lowest consumers.  
3. Calculate total water consumption.  
4. Categorize houses:  
o Low (<2000 litres)  
o Medium (2000–3500 litres)  
o High (>3500 litres)  
5. Count households eligible for conservation awareness programs (>2500 litres).  '''

water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}

print("Houses Consuming More Than 3000 Litres:")
for house, litres in water_usage.items():
    if litres > 3000:
        print(house)

highest = max(water_usage, key=water_usage.get)
lowest = min(water_usage, key=water_usage.get)

print("Highest Consumption:")
print(highest, "(", water_usage[highest], "litres )")

print("Lowest Consumption:")
print(lowest, "(", water_usage[lowest], "litres )")

total = sum(water_usage.values())
print("Total Consumption:", total, "litres")

low = []
medium = []
high = []

eligible = 0

for house, litres in water_usage.items():
    if litres < 2000:
        low.append(house)
    elif litres <= 3500:
        medium.append(house)
    else:
        high.append(house)

    if litres > 2500:
        eligible += 1

print("Low Consumption:")
print(low)

print("Medium Consumption:")
print(medium)

print("High Consumption:")
print(high)

print("Eligible Households:", eligible)

'''
Sample Output 
Houses Consuming More Than 3000 Litres: 
House103 
House106 
House108 
House110 
 
Highest Consumption: 
House110 (4500 litres) 
 
Lowest Consumption: 
House109 (1500 litres) 
 
Total Consumption: 28,300 litres 
 
Low Consumption: 
['House101', 'House105', 'House109'] 
 
Medium Consumption: 
['House102', 'House103', 'House104', 'House107'] 
 
High Consumption: 
['House106', 'House108', 'House110'] 
 
Eligible Households: 5
