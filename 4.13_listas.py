# Armazenar 5 refeições em uma Tupla
lunch = ('Arroz com Feijão', 'Macarronada', 'Marmita de Bife', 'Lasanha',
'Hot Dog')

# exibir cada refeição que o restauranteco serve
for ref in lunch:
    print(ref)
print()    

# Tente modificar um dos elementos
'''
lunch[4] = 'Cheseburger'
print(lunch)

TypeError: 'tuple' object does not support item assignment
'''
# Reformular o menu com substituição de dois itens
print()
new_lunch = ('Arroz á Grefa', 'Macarronada á Bolanhesa', 'Marmita de Bife', 'Lasanha',
'Hot Dog')

print(lunch)
print()
print(new_lunch)