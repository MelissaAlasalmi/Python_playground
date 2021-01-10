import numpy as np

height_in = [74, 74, 72, 75, 75, 73]
weight_lb = [180, 215, 210, 188, 200, 180]

# Create an array of heights in inches
np_height_in = np.array(height_in)
print("Heights in inches: " + str(np_height_in))
print(type(np_height_in))

# Convert hights in inches to heights in meters
np_height_m = np_height_in * 0.0254
print("Heights in meters: " + str(np_height_m))
print(type(np_height_m))

# Create an array of weights in pounds
np_weight_lbs = np.array(weight_lb)
print("Weights in pounds: " + str(np_weight_lbs))
print(type(np_weight_lbs))

# Convert wights in pounds to weights in kilos
np_weight_kg = np_weight_lbs * 0.453592
print("Weights in kilos: " + str(np_weight_kg))
print(type(np_weight_kg))

# Calculate the BMI
bmi = np_weight_kg / (np_height_m ** 2)
print("BMI: " + str(bmi))
print(type(bmi))

# Create an array to test if the bmi is over '24'
over_tf = bmi > 24
print("Are theses BMIs over 24? " + str(over_tf))
print(type(over_tf))

# Print only those BMIs from the 'bmi' array that are over '24'
print("BMIs over 24: " + str(bmi[over_tf]))
