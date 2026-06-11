''' City Population & Development Dashboard 
Problem Statement 
The government wants to analyze city data. 
Store details of at least 30 cities. 
Example Structure 
cities = { 
    "Delhi": { 
        "population": 32000000, 
        "area": 1484, 
        "literacy": 89 
    } 
} 
Requirements 
1. Display all city details.  
2. Find the most populated city.  
3. Find the least populated city.  
4. Calculate average population.  
5. Display cities with literacy rate above 90%.  
6. Display cities with literacy below average.  
7. Calculate population density.  
8. Find city with highest density.  
9. Categorize cities:  
o Small  
o Medium  
o Large  
10. Create a development-priority list.  
11. Generate separate dictionaries for:  
o High Literacy Cities  
o Low Literacy Cities  
12. Generate a national summary report.  
Challenge 
Rank all cities based on population density. '''


# City Population & Development Dashboard

# Store details of 30 cities
cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 91},
    "Kolkata": {"population": 15000000, "area": 205, "literacy": 87},
    "Chennai": {"population": 11000000, "area": 426, "literacy": 90},
    "Bengaluru": {"population": 13000000, "area": 741, "literacy": 92},
    "Hyderabad": {"population": 10000000, "area": 650, "literacy": 88},
    "Ahmedabad": {"population": 8500000, "area": 505, "literacy": 86},
    "Pune": {"population": 7500000, "area": 331, "literacy": 91},
    "Jaipur": {"population": 4000000, "area": 467, "literacy": 84},
    "Lucknow": {"population": 3800000, "area": 349, "literacy": 82},

    "Kanpur": {"population": 3200000, "area": 403, "literacy": 79},
    "Nagpur": {"population": 3000000, "area": 227, "literacy": 89},
    "Indore": {"population": 2800000, "area": 530, "literacy": 87},
    "Bhopal": {"population": 2500000, "area": 463, "literacy": 85},
    "Patna": {"population": 2600000, "area": 250, "literacy": 81},
    "Surat": {"population": 7000000, "area": 474, "literacy": 88},
    "Vadodara": {"population": 2200000, "area": 220, "literacy": 90},
    "Agra": {"population": 1800000, "area": 121, "literacy": 78},
    "Varanasi": {"population": 1600000, "area": 112, "literacy": 77},
    "Meerut": {"population": 1700000, "area": 450, "literacy": 76},

    "Nashik": {"population": 2000000, "area": 259, "literacy": 86},
    "Rajkot": {"population": 1900000, "area": 170, "literacy": 89},
    "Coimbatore": {"population": 2100000, "area": 246, "literacy": 92},
    "Madurai": {"population": 1800000, "area": 148, "literacy": 88},
    "Mysuru": {"population": 1200000, "area": 286, "literacy": 91},
    "Ranchi": {"population": 1400000, "area": 175, "literacy": 83},
    "Raipur": {"population": 1500000, "area": 226, "literacy": 84},
    "Guwahati": {"population": 1300000, "area": 216, "literacy": 85},
    "Chandigarh": {"population": 1100000, "area": 114, "literacy": 93},
    "Dehradun": {"population": 1000000, "area": 300, "literacy": 89}
}


# 1. Display all city details
print("All City Details:")

for city, details in cities.items():
    print(city, "Population:", details["population"], "Area:", details["area"], "Literacy:", details["literacy"])


# 2. Find the most populated city
city_items = list(cities.items())

most_city = city_items[0][0]
most_population = city_items[0][1]["population"]

for city, details in cities.items():
    if details["population"] > most_population:
        most_population = details["population"]
        most_city = city

print()
print("Most Populated City:")
print(most_city, "Population:", most_population)


# 3. Find the least populated city
least_city = city_items[0][0]
least_population = city_items[0][1]["population"]

for city, details in cities.items():
    if details["population"] < least_population:
        least_population = details["population"]
        least_city = city

print()
print("Least Populated City:")
print(least_city, "Population:", least_population)


# 4. Calculate average population
total_population = 0

for details in cities.values():
    total_population = total_population + details["population"]

average_population = total_population / len(cities)

print()
print("Average Population:", average_population)


# 5. Display cities with literacy rate above 90%
print()
print("Cities With Literacy Rate Above 90%:")

for city, details in cities.items():
    if details["literacy"] > 90:
        print(city, "Literacy:", details["literacy"])


# Calculate average literacy for requirement 6
total_literacy = 0

for details in cities.values():
    total_literacy = total_literacy + details["literacy"]

average_literacy = total_literacy / len(cities)


# 6. Display cities with literacy below average
print()
print("Average Literacy:", average_literacy)

print()
print("Cities With Literacy Below Average:")

for city, details in cities.items():
    if details["literacy"] < average_literacy:
        print(city, "Literacy:", details["literacy"])


# 7. Calculate population density
# Population density = population / area
print()
print("Population Density of Cities:")

for city, details in cities.items():
    density = details["population"] / details["area"]
    details["density"] = density

    print(city, "Density:", density)


# 8. Find city with highest density
highest_density_city = city_items[0][0]
highest_density = cities[highest_density_city]["density"]

for city, details in cities.items():
    if details["density"] > highest_density:
        highest_density = details["density"]
        highest_density_city = city

print()
print("City With Highest Density:")
print(highest_density_city, "Density:", highest_density)


# 9. Categorize cities: Small, Medium, Large
# Small: population < 20 lakh
# Medium: 20 lakh to 1 crore
# Large: above 1 crore
small_cities = []
medium_cities = []
large_cities = []

for city, details in cities.items():
    population = details["population"]

    if population < 2000000:
        small_cities.append(city)
    elif population <= 10000000:
        medium_cities.append(city)
    else:
        large_cities.append(city)

print()
print("Small Cities:")
print(small_cities)

print()
print("Medium Cities:")
print(medium_cities)

print()
print("Large Cities:")
print(large_cities)


# 10. Create a development-priority list
# Cities with literacy below average are given development priority
development_priority = []

for city, details in cities.items():
    if details["literacy"] < average_literacy:
        development_priority.append(city)

print()
print("Development Priority List:")
print(development_priority)


# 11. Generate separate dictionaries for high literacy and low literacy cities
high_literacy_cities = {}
low_literacy_cities = {}

for city, details in cities.items():
    if details["literacy"] >= 90:
        high_literacy_cities[city] = details
    else:
        low_literacy_cities[city] = details

print()
print("High Literacy Cities:")

for city, details in high_literacy_cities.items():
    print(city, "Literacy:", details["literacy"])

print()
print("Low Literacy Cities:")

for city, details in low_literacy_cities.items():
    print(city, "Literacy:", details["literacy"])


# 12. Generate national summary report
print()
print("========== NATIONAL SUMMARY REPORT ==========")

print("Total Cities:", len(cities))
print("Total Population:", total_population)
print("Average Population:", average_population)
print("Average Literacy:", average_literacy)
print("Most Populated City:", most_city)
print("Least Populated City:", least_city)
print("Highest Density City:", highest_density_city)
print("Small Cities Count:", len(small_cities))
print("Medium Cities Count:", len(medium_cities))
print("Large Cities Count:", len(large_cities))
print("Development Priority Cities:", len(development_priority))

print("============================================")


# Challenge: Rank all cities based on population density
density_ranking = list(cities.items())

# Sort cities according to density in descending order
density_ranking.sort(key=lambda x: x[1]["density"], reverse=True)

print()
print("Cities Ranked By Population Density:")

rank = 1

for city, details in density_ranking:
    print(rank, city, "Density:", details["density"])
    rank = rank + 1

