rivers = {
    'danube': 'romania',
    'thames': 'united kingdom',
    'nile': 'egypt',
    }

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}")
    print(f"\n{river.title()}")
    print(f"\n{country.title()}")
