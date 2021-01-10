import pandas as pd
import numpy as np 

# Import cars.csv data:
cars = pd.read_csv('cars.csv')

# Extract drives_right column as a series
dr = cars['drives_right']

# Use dr to subset cars
sel = cars[dr]
print(sel)

# Convert the code above to a one-liner
sel = cars[cars['drives_right']]
print(sel)

# Observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_manic = cars[many_cars]
print(car_manic)

# Convert the code above to a one-liner
car_manic = cars[cars['cars_per_cap'] > 500]
print(car_manic)

# Observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc >= 100, cpc <= 500)
medium = cars[between]
print(medium)
