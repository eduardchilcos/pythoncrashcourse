guests = ['Mama Leone', 'Ronald McDonald', 'Shrek', 'Scooby Doo']
print(f"Hey, {guests[0]}! I would like to kindly invite you to dinner this week.")
print(f"Good evening, {guests[1]}! Let's have some of that awful food from the placed named after you.")
print(f"Hey {guests[2]}, would you like to join me, {guests[3]} and other imaginary friends for dinner this week?")

uninvited = guests.pop(0)
print(f"Sadly {uninvited} is not going to be able to make it.")

guests.append('Ash Ketchum')
print(f"Hey, {guests[0]}! I would like to kindly invite you to dinner this week.")
print(f"Good evening, {guests[1]}! Let's have some of that awful food from the placed named after you.")
print(f"Hey {guests[2]}, would you like to join me, {guests[3]} and other imaginary friends for dinner this week?")

guests.insert(0, 'Bill Gates')
guests.insert(3, 'George Soros')
guests.insert(7, 'Kanye West')

print(f"Hey, {guests[0]}! I would like to kindly invite you to dinner this week.")
print(f"Good evening, {guests[1]}! Let's have some of that awful food from the placed named after you.")
print(f"Hey {guests[2]}, would you like to join me, {guests[3]} and other imaginary friends for dinner this week?")
print(f"I'd love you to join us for dinner, {guests[4]}.")
print(f"We're throwing a dinner get-together at mine next week, wanna join {guests[5]}?")
print(f"Remember that dinner party I've been meaning to organise? It's scheduled for next week, {guests[6]}.")

print("Sadly, we'll only be able to accomodate for two people for next weekend's dinner.")
print(guests)

removed_guest = guests.pop()
print(f"Sorry, {removed_guest} unfortunately you have been uninvited. Bye!")
print(guests)

removed_guest = guests.pop()
print(f"Sorry, {removed_guest} unfortunately you have been uninvited. Bye!")
print(guests)

removed_guest = guests.pop()
print(f"Sorry, {removed_guest} unfortunately you have been uninvited. Bye!")
print(guests)

removed_guest = guests.pop()
print(f"Sorry, {removed_guest} unfortunately you have been uninvited. Bye!")
print(guests)

removed_guest = guests.pop()
print(f"Sorry, {removed_guest} unfortunately you have been uninvited. Bye!")
print(guests)

print(f"Hi {guests[0]}, you're still invited!")
print(f"Heya {guests[1]} just to let you know that you're still invited!")

del guests[0]
del guests[0]
print(guests)