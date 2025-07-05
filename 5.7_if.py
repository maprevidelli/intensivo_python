#Frutas favoritas
favorite_fruits = ['banana', 'manga', 'mamão', 'pêra']
for fruta in favorite_fruits:
    if fruta == 'banana':
        print(f'que delícia de {fruta}, parace um macaco comendo!')
    elif fruta == 'manga':
        print(f'Olhá só agora ta comendo {fruta}, que nem um cão chupando..')
    elif fruta == 'mamão':
        print(f'{fruta}!!, tá querendo rechear o vaso sanitário hein..')
    elif fruta == 'pêra':
        print(f'Nossa comendo uma {fruta}, que delicinha!')
print()
outra = input('Que fruta você come?: ')
if outra in favorite_fruits:
    print(f'Minha nossa nossa nossa! você gosta de {outra} mesmo hein')
else:
    print(f'{outra}, não está nas suas favoritas..')    