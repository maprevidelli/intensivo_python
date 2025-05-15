# 3.9
cidades = ['Hong Kong', 'Manchester', 'Roma', 'Napoli', 'Amsterdan']
opcao = [0, 1, 2, 3, 4]
term = True
while term:
    try:
        escolha = int(input('Entre com a opção: '))
        if escolha not in opcao:
            print('Fora da Range')
            continue
    except ValueError:
        print('opção inválida!') 
        continue 
    print(f'Cidade escolhida foi:{cidades[escolha]}')
    term = False
