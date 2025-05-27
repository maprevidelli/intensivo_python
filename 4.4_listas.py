# 4.4 crie uma lista de 1 a 1 milhão
lista = []
numero = 0
for cont in range (1, 1000001):
    numero += 1
    lista.append(numero)
for item in lista:
    print(item)
