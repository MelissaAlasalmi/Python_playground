numbers = [23, 24, 93, 23, 432, 3, 254]
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]

#takes each of the numbers in 'numbers' and multiplies them by 2
for i in range(0, len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

#prints all the numbers in 'numbers' and their index
for index, num in enumerate(numbers):
    print("index " + str(index) + ": " + str(num))

#prints all the 'spaces' in 'areas' and their 'room' number in a human-friendly way
for index, spaces in enumerate(areas):
    print("room " + str(index + 1) + ": " + str(spaces))
         
#prints all the 'rooms' and 'areas' in 'house'
for rooms, areas in house :
    print("the " + rooms + " is " + str(areas) + " sqm")