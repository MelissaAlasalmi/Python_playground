import pandas as pd
cars = pd.read_csv('cars.csv')

# Print out country column as Pandas Series
print(str(cars['country']))
print(type(cars['country']))

# Print out country column as Pandas DataFrame
print(str(cars[['country']]))
print(type(cars[['country']]))

# Print out DataFrame with country and drives_right columns
print(str(cars[['country', 'drives_right']]))
print(type(cars[['country', 'drives_right']]))