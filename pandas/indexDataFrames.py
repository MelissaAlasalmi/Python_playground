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

# Print out first 3 rows
print(str(cars[0:3]))

# Print out fourth, fifth and sixth rows
print(str(cars[3:6]))

# Print out series for Japan
print(str(cars.loc['JPN']))

# Print out dataframe for Australia and Egypt
print(str(cars.loc[['AUS', 'EG']]))

# Print out the 'drives_right' value of Morocco
print(str(cars.loc['MOR', 'drives_right']))

# Print a sub-DataFrame containing, for Russia and Morocco, the columns 'country' and 'drives_right'
print(str(cars.loc[['RU', 'MOR'], ['country', 'drives_right']]))

# Print out drives_right column as Series
print(str(cars.loc[:, 'drives_right']))

# Print out drives_right column as DataFrame
print(str(cars.loc[:, ['drives_right']]))

# Print out cars_per_cap and drives_right as DataFrame
print(str(cars.loc[:, ['cars_per_cap', 'drives_right']]))