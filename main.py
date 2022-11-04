import random
import pandas as pd
from string import ascii_uppercase


# listy z odpowiedziami
cities = pd.read_csv('cities.csv')
countries = pd.read_csv('countries.csv')
country_list = countries['name'].apply(lambda x: x.lower()).unique()
city_list = cities['city_name'].apply(lambda x: x.lower()).unique()
categories = {"City": city_list,
              "Country": country_list,
              }

# gameloop
flag = True
while flag:
    game_letter = random.choice(ascii_uppercase)
    print(f'Game letter: {game_letter}')
    # tu widzimy co zostalo zgadniete
    not_guessed = list(categories.keys())
    while not_guessed:
        current_categories = not_guessed.copy()
        for category in current_categories:
            print(f'{category}:')
            guess = input(f"Guess: ").lower()
            if guess[0].upper() == game_letter and guess in categories[category]:
                print(f'Valid {category}')
                not_guessed.remove(category)
    print("-" * 100)
