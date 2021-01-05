numbers = [43, 543, 3423, -343, -1, 0 , 343, 2, 35, -34567, -14]

#takes each of the numbers in 'numbers' and checks if they are greater than zero
for number in numbers:
    if number > 0:
        print(str(number) + " is greater than zero.")
    else:
        print(str(number) + " is not greater than zero.")