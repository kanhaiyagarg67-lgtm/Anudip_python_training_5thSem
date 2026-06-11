 #Program for water tank filling
water_level = 0  # initialy water level is 0 
while water_level <= 100: # run until 100 litres
    water_level += 10 # increase level by 10% in each minute
    print("Water level: ", water_level, "litres")
print("Water tank is full.")
