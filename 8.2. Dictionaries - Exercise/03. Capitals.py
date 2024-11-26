country = input().split(', ')
capitals = input().split(', ')

information = dict(zip(country, capitals))
for country, capitals in information.items():
    print(f'{country} -> {capitals}')
