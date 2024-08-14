# 1. Declare and assign the variables here:
shuttle_name = 'Determination'
shuttle_speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 38400
MILES_PER_KM = 0.621
# 2. Use print() to print the 'type' each variable. Print one item per line.

print("shuttle_name type:  " + str(type(shuttle_name)))
print("shuttle_speed_mph type:  " + str(type(shuttle_speed_mph)))
print("distance_to_mars_km type:  " + str(type(distance_to_mars_km)))
print("distance_to_moon_km type:  " + str(type(distance_to_moon_km)))
print("MILES_PER_KM type:  " + str(type(MILES_PER_KM)))
# Code your solution to exercises 3 and 4 here:
miles_to_mars = distance_to_mars_km * MILES_PER_KM
hours_to_mars = miles_to_mars / shuttle_speed_mph
days_to_mars = hours_to_mars / 24

print (shuttle_name + " will take " + str(days_to_mars) + " days to reach Mars.")
# Code your solution to exercise 5 here
miles_to_moon = distance_to_moon_km * MILES_PER_KM
hours_to_moon = miles_to_moon / shuttle_speed_mph
days_to_moon = hours_to_moon / 24
print(shuttle_name + " will take " + str(days_to_moon) + " days to reach the Moon.")