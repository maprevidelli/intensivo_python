# 2.3
nome_user = input('Hello, what is your name?: ')
print(f'Olá {nome_user}, gostaria de aprender um pouco de Python hoje?')

# 2.4
nome_maiusculo = nome_user.capitalize()
nome_minusculo = nome_user.lower()
print(nome_minusculo)
print(nome_maiusculo)

# 2.6
famous_person = "Albert Einstein"
message = "Uma pessoa que nunca cometeu um erro nunca tentou nada de novo"
print(f'{famous_person} disse uma vez: "{message}"')

# 2.7
name = '   Darth Vader '
print(f'\no nome em destaque é:{name}\n \tquer voce queria ou não!')
print('='* 45)
print(f'Remover espaço na esquerda: {name.lstrip()}')
print(f'Remover espaço na direita: {name.rstrip()}')
print(f'ambos lados: {name.strip()}')

# 2.8
filename = 'python_notes.txt'
print(f'Remove Sulfixo: {filename.removesuffix(".txt")}')
print(f'Remove prefixo: {filename.removeprefix("python_")}')
