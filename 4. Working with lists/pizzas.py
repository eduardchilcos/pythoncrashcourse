pizzas = ['pepperoni', 'texas bbq', 'meateor', 'mighty meaty', 'chicken feast', 'american hot']
for pizza in pizzas:
    print(f"{pizza.title()} has always been my favourite.")

print("\nI always think\n that words cannot express\n how much I REALLY LOVE PIZZA!!!")

friend_pizzas = pizzas[:]

pizzas.append('capriciosa')
friend_pizzas.append('hawaiian')

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)