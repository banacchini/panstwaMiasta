import pandas as pd
from string import ascii_uppercase

data = pd.read_csv('worldcities.csv')
data["first_letter"] = data["city_ascii"].str[0]
data = data[["city_ascii", "first_letter"]].rename({"city_ascii": "city_name"}, axis=1)
data = data.drop_duplicates()
data = data[data["first_letter"].isin(list(ascii_uppercase))]

print(data["first_letter"].value_counts())
print(" ")
print(data.head())
