'''3. City Temperature Monitoring System 
Problem Statement 
Daily temperatures of different cities are stored as: 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1. Display cities having temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (temperature < 35°C).  
6. Count cities with temperature between 35°C and 40°C.  
Sample Output 
Cities Above 40°C: 
Delhi 
Jaipur 
Ahmedabad 
 
Hottest City: Ahmedabad (43°C) 
 
Coolest City: Bengaluru (28°C) 
 
Average Temperature: 36.8°C 
 
Pleasant Cities: 
['Mumbai', 'Bengaluru', 'Pune'] 
 
Cities Between 35°C and 40°C: 4'''

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Display cities having temperature above 40°C
print("Cities Above 40°C:")

for city, temp in temperature.items():
    if temp > 40:
        print(city)


# 2. Find the hottest city
# First city ko hottest maan liya
dict_items = list(temperature.items())

hottest_city = dict_items[0][0]
highest_temp = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_temp:
        hottest_city = item[0]
        highest_temp = item[1]

print()
print("Hottest City:", hottest_city, highest_temp ,"°C")


# 3. Find the coolest city
# First city ko coolest maan liya
coolest_city = dict_items[0][0]
lowest_temp = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_temp:
        coolest_city = item[0]
        lowest_temp = item[1]

print()
print("Coolest City:", coolest_city, lowest_temp ,"°C")


# 4. Calculate average temperature
total = 0

for temp in temperature.values():
    total = total + temp

average = total / len(temperature)

print()
print("Average Temperature:", average, "°C")


# 5. Create a list of pleasant cities
pleasant_cities = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print()
print("Pleasant Cities:")
print(pleasant_cities)


# 6. Count cities with temperature between 35°C and 40°C
count = 0

for temp in temperature.values():
    if temp >= 35 and temp <= 40:
        count = count + 1

print()
print("Cities Between 35°C and 40°C:", count)
