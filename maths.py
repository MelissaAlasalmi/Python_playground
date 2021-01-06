import math

radius = 0.43

# Calculate the circumference and area of a circle
circumference = (2 * math.pi) * radius
area = math.pi * (radius ** 2)
print("Circumference: " + str(circumference))
print("Area: " + str(area))

radius = 192500

# Calculate the travel distance of a moon over 12 degrees.
phi = math.radians(12)
dist = radius * phi
print("Distance: " + str(dist))