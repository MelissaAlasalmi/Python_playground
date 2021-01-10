
place = "poolhouse"
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use upper() on 'place'
place_up = place.upper()
print(place), print(place_up)

# Print the number of 'o's in 'place'
print(place.count("o"))

# Print the index of the element '20.0'
print(areas.index(20.0))

# Use append twice to add poolhouse and garage sizes to 'areas'
areas.append(24.5)
areas.append(15.45)
print(areas)

# Reverse the order of the elements in 'areas'
areas.reverse()
print(areas)