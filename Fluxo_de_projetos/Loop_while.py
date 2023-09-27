tentativas = 0

while tentativas < 3:
    print('Tente novamente')
    tentativas += 1

senha = ''
while senha != '12345':
    senha = input('Senha: ')
print('Bem-Vindo!')

nome = ''
while nome == '':
    nome = input('Nome: ')
print(f'Bem-Vindo {nome}')


# DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120
cont = 1
while cont <= 120:
    print(f'-> {cont}')
    cont += 1

# DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'
senha = ''
while senha != 'secreto':
    senha = input('Senha: ')
print('Acesso Concluido!')

# DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente de 100 para 1
cont = 100
while cont != 0:
    print(f'-> {cont}')
    cont -= 1
