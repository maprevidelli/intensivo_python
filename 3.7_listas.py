#3.7
convidados = ['Mr. Spock', 'Captain Kirk', 'Han Solo', 'Shewbaca', 'Darth Vader']
for convite in convidados:
    print(f'Carissímo {convite}! você está convidado para o jantar espacial especial')
print()    
print(f'Informamos que o convidado {convidados[1]} não estará no evento por motivos não divulgados')  
convidados[1] = 'Jaba de Hut'
print(f'Nobre {convidados[1]}, você está conidado para o terrível \
jantar especial espacial')
print('==='* 40)
print('Está disponível uma mesa maior!')
convidados.insert(0, 'Princesa Lea')
convidados.insert(3, 'Bobba Fett')
convidados.append('Sonda Bi-Atenction')
print('==='* 40)
for convite in convidados:
    print(f'Nobre {convite}, você foi convidado para a mesa VIP')
print('==='* 40)
print('Lamentamos o transtorno mas somente 2 convidados estarão no jantar!')
print('==='* 40)
print(convidados)
print('==='* 40)
#for excluidos in convidados:
#    fora = convidados.pop()
#    print(f'Ilustre {fora}, infelismente você foi desconvidado!')
# veja que desta maneira a lista para em 4, pois ela foi programada e inciada 
# em uma iteração para 8 itens, mas quando chega a 4 ela para pois foi diminuida
# 4 vezes alem da iteração, totalizando 8 ciclos.
# PARA CORRIGIR teriamos que reservar os 2 ultimos ou usar um While até os 2 ultimos
print('==='* 40)
# Separando os 2 últimos:
for excluido in convidados[2:]:
    print(f'Ilustre {excluido}, infelismente você fora desconvidado!')
convidados_2 = convidados[:2] # uma cópia para os 2 primeiros   
print()
print(convidados_2)
print('==='* 40)
# Através de um While:
while len(convidados) > 2:
    fora = convidados.pop()
    print(f'{fora}, Você foi chutado do jantar Espacial!')
print()
print(convidados)
print('==='* 40)
# removendo o restante com o Del
del convidados[:2]# exclui o 0 e o 1, nunca remove o setado/ultimo, no caso 2
print(f'Lista vazia: {convidados}')
