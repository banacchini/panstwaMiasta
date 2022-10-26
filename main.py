import pandas as pd

data = pd.read_csv('worldcities.csv')
cities = list(data.city_ascii)
print(cities)

if "Tokyo" in cities:
    print('hurra')