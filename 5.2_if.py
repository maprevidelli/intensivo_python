# Testes condicionais
cor = 'azul'

print(cor == 'azul')
print(cor != 'azul')
print(cor.lower())

if cor == 'azul':
    print('Minusculo')
else:
    print('MAIUSCULA') 

print()       

numero = 0
if numero > 1:
    print('maior')
else:
    print('menor')

lista = [x for x in range(6)]    
print(lista)
print(4 in lista)
print(10 in lista)