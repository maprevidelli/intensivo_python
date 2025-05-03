# 3.4
convidados = ['Mr. Spock', 'Captain Kirk', 'Han Solo', 'Shewbaca', 'Darth Vader']
for convite in convidados:
    print(f'Carissímo {convite}! você está convidado para o jantar espacial especial')
print()    
# 3.5
print(f'Informamos que o convidado {convidados[1]} não estará no evento por motivos não divulgados')  
convidados[1] = 'Jaba de Hut'
print(f'Nobre {convidados[1]}, você está conidado para o terrível \
jantar especial espacial')