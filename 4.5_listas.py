# 4.5 
lista = []
numero = 0
for cont in range (1, 1000001):
    numero += 1
    lista.append(numero)
for item in lista:
    print(item)
print(min(lista), max(lista))    