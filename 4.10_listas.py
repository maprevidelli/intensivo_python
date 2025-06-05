# 4.10 Fatias em Listas

english_teams = ['Manchester Utd', 'Liverpool', 'Arsenal', 'Chelsea', 'Aston Vila',
         'Totteham', 'BlackBurn', 'Manchester City', 'Corinthians Casuals']

print(f'Os três primeiro elementos da lista são: ',english_teams[0:3])
print()
print(f'OS três elementos do meio na lista são: ', english_teams[3:6])
print()
print(f'Os três utimos elementos da lista são: ', english_teams[:-4:-1])

# 4.11 Minhas pizzas, suas pizzas
print('\n###')

pizzas = ['Atum', 'Calabresa', 'Quatro-Queijos']
friend_pizzas = pizzas.copy()

pizzas.append('Peperoni')
friend_pizzas.append('Luborguing')

for item in pizzas:
    print(f'Minhas pizzas favoritas são: {item}')


for iten in friend_pizzas:
    print(f'as dos amigos são: {iten}')
    
