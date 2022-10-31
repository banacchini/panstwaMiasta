import pandas as pd
import random
from string import ascii_uppercase

cities = pd.read_csv('cities.csv')
countries = pd.read_csv('countries.csv')
country_list = countries['name'].apply(lambda x: x.lower()).unique()
while True:
    game_letter = random.choice(ascii_uppercase)
    print(f'Game letter: {game_letter}')
    guessed = False
    while not guessed:
        country = input('Country: ').lower()
        if country[0].upper() == game_letter and country in country_list:
            print('Valid country!')
            guessed = True

