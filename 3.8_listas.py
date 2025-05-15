#Exercicio 3.8
cidades = ['Hong Kong', 'Manchester', 'Roma', 'Napoli', 'Amsterdan']
print(f'a) {cidades}')
# use o sorted, pois ele nao altera a original, diferente do sort()
print(f'b){sorted(cidades)}')
# Mostre a original sem alterações
print(f'c) {cidades}')
# use o Sorted como reversa para nao alterar a original
print(f'd) {sorted(cidades, reverse=True)}')
# mostre a original mais uma vez
print(f'e) {cidades}')
# use o Reverse
cidades.reverse()
print(f'f){cidades}')
# Voltando ao original
cidades.reverse()
print(f'g) {cidades}')
# use o Sort()
cidades.sort()
print(f'h) {cidades}')
# use o Sort() de forma inversa
cidades.sort(reverse=True)
print(f'i) {cidades}')