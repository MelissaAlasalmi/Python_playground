import numpy as np 
import pandas as pd

europe = {'spain':'madrid', 
          'france':'paris', 
          'germany':'berlin', 
          'norway':'oslo', 
          'austria':'vienna'}

bmi = np.array([[1.88, 1.88, 1.82, 1.91,  1.91,  1.85],
                  [81.6, 97.5, 95.3, 85.3, 90.7, 81.6]])

cars = pd.read_csv('cars.csv')

#prints all the capitals ('value') of countries ('key') in a dictionary
for key, value in europe.items() :
    print("the capital of " + key + " is " + value)

#prints all the bmi's ('value') of combined 'height' and 'weight' in a 2D numpy array
height = bmi[0]
weight = bmi[1]
for value in np.nditer(weight / (height ** 2)) :
    print("the bmi is " + str(value))

#prints every single 'value' in the 2D numpy array 'bmi'
for value in np.nditer(bmi) :
    print(str(value))

#prints every single 'row' in the pandas dataframe 'cars' + lables
for lable, row in cars.iterrows() :
    print(lable)
    print(row)

#prints only the 'lable' and the 'country' of each dataframe 'cars'
for lable, row in cars.iterrows() :
    print(lable + ": " + row["country"])

#applys 'namlen' collumn to 'cars' then prints the 'country' and the 'namlen' of each country from each dataframe
cars["namlen"] = cars["country"].apply(len)
print(cars)
for lable, row in cars.iterrows() :
    print("the length of " + row["country"] + " is " + str(row["namlen"]))
