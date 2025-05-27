# multiplos de 3 a 30
lista = []
numero = 1
for cont in range (1, 31):
    if cont % 3 == 0:
        lista.append(cont)
print(lista)        