# olá admin
users = ['Joncarlos', 'Marinayara', 'Carlino', 'Admin', 'Novalgildo']
#users = []
if len(users) == 0:
    print('é necessário encontrar alguns usuários!')

for user in users:
    print(f'Olá {user}, está logado agora!')
    if user == 'Admin':
        print('Olá Administrador! gostaria de ver algum relatório?')
    else:
        print(f'{user}, Bem vindo ao sistema novamente')
