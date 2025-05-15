# 3.6
convidados = ['Mr. Spock', 'Captain Kirk', 'Han Solo', 'Shewbaca', 'Darth Vader']
for convite in convidados:
    print(f'\nCarissímo {convite}! você está convidado para o jantar espacial especial')
print()    
# 3.5
print(f'Informamos que o convidado {convidados[1]} não estará no evento por motivos não divulgados')  
convidados[1] = 'Jaba de Hut'
print(f'Nobre {convidados[1]}, você está conidado para o terrível \
jantar especial espacial')
print('==='* 40)
print('Está disponível uma mesa maior!')
convidados.insert(0, 'Princesa Lea')
convidados.insert(3, 'Bobba Fett')
convidados.append('Sonda Bi-Atenction')
print(convidados)
print('==='* 40)
for convite in convidados:
    print(f'Nobre {convite}, você foi convidado para a mesa VIP')