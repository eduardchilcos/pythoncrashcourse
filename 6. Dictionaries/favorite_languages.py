favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

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

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())