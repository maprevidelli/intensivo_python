# números ímpares
lista = []
num = 1
for cont in range(1, 21):
    lista.append(num)
    num += 1
print(lista)
for cont in range(0, 20, 2):
    print(lista[cont])
