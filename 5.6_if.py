# Frases da vida
age = float(input('Entre com a sua idade: '))
if age < 2:
    print('Você ainda é neném!')
elif age >= 2 and age < 4:
    print('Criança você!')
elif age >= 4 and age < 13:
    print('Garoto você é!')        
elif age >= 13 and age < 20:
    print('Aborrecente você!')
elif age >= 20 and age < 65:
    print('Adulto!')
elif age >= 65:
    print('idoso!')
else:
    print('digitou uma merda!')

