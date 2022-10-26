import pandas as pd
data = pd.read_csv('worldcities.csv')
cities = data.city
print(cities)
if "Wroclaw" in cities:
    print('hurra')