# cores de alienigenas
alien_color = input('Cor do alienigêna - \n(amarelo)\n(verde)\n(vermelho)\nDigite: ')
if alien_color == 'verde':
    print('Ganhou 5 pontos por abater o alíenigena!')
elif alien_color == 'vermelho' or alien_color =='amarelo':
    print('Ganhou 10 pontos! Alien abatido!')
else:
    print('Desses ainda não baixaram na Terra')    

