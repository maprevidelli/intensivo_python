# 4.8 Cubos
lista = []
numero = 1
for cont in range (0, 10):
    lista.append(numero)
    numero += 1
 
for num in lista:
    cubo = num ** 3
    print(f'{num} ao cubo é = {cubo}')

# 4.9 List Comprehension
i = 1
nova = [i ** 3 for i in range (11)]
print(nova)
