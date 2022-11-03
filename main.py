import pandas as pd
import random
from string import ascii_uppercase

#listy z odpowiedziami
cities = pd.read_csv('cities.csv')
countries = pd.read_csv('countries.csv')
country_list = countries['name'].apply(lambda x: x.lower()).unique()
categories = {"City" : cities,
              "Country" : country_list,
              }

#gameloop
flag = True
while flag:
    game_letter = random.choice(ascii_uppercase)
    print(f'Game letter: {game_letter}')
    guessed = False
    while not guessed:
        for category in categories.keys():
            print(f"{category}:")
            guess = input(f"Guess: ").lower()
            if guess[0].upper() == game_letter and guess in categories[category]:
                print(f'Valid {category}')
                guessed = True
