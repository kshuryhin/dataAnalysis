import pandas as pd

#Task 1
pokemon = pd.read_csv('pokemon.csv', usecols=['name', 'generation', 'type1', 'type2', 'hp', 'speed', 'sp_attack', 'sp_defense', 'abilities'])
pokemon = pokemon[322:757]
pokemon['abilities'] = pokemon['abilities'].str.replace('[', '')
pokemon['abilities'] = pokemon['abilities'].str.replace(']', '')
pokemon[['abilities1', 'abilities2', 'abilities3', 'abilities4', 'abilities5', 'abilities6']] = pokemon['abilities'].str.split(',',
                                                                                                                                expand=True)
pokemon_updated = pokemon.to_csv('pokemon_updated.csv')
# print(pokemon.head(5))

#Task 2
# print(pokemon.index)
# print()
# print(pokemon.columns)

#Task 3
# print(pokemon[2:267])

#Task 4
# print(pokemon.loc[:, ['generation', 'type1', 'type2', 'hp', 'speed']])

#Task 5
# print(pokemon['name'].sort_values(ascending=True))

#Task 6
# print(pokemon[pokemon['hp'] > 38])

#Task 7
# print(pokemon[(pokemon['type1'] == 'grass') & (pokemon['speed'] > 41) & (pokemon['type2'] == 'steel')])

#Task 8
print(pokemon.loc[(pokemon['sp_attack'] > 30) & (pokemon['sp_defense'] > 80), ['name', 'generation']])
