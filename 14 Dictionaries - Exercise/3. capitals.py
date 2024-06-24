country_names = input().split(', ')
capitals = input().split(', ')

country_names_and_capitals = dict(zip(country_names, capitals))

for country, capital in country_names_and_capitals.items():
    print(f'{country} -> {capital}')
