'''favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }'''

'''language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")'''

'''for name in favourite_languages.keys():
    print(name.title())'''

'''friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")'''

'''for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")'''

'''print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())'''

'''people = ['marcus', 'andrew', 'natalie', 'sophie', 'lucy', 'sarah', 'edward']

for name in people:
    if name in favourite_languages.keys():
        print(f"\nThanks for taking the poll, {name.title()}.")
    else:
        print(f"\nYou've yet to take the poll, {name.title()}. Please do so.")'''

favourite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favourite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favourite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    elif len(languages) == 1:
        favourite_language = languages[0]  # Explicitly extract the single language
        print(f"\n{name.title()}'s favourite language is {favourite_language.title()}.")
    else:
        print(f"\n{name.title()} has not specified a favourite language.")
