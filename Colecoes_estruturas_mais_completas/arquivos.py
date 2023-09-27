# Como salvar informações em um arquivo [Pesquisar, Salvar, Editar, Excluir]

'''
-> CRIAR E MODIFICAR ARQUIVOS
"r" -> Usado somente para LER algo
"w" -> Usado somente para ESCREVER algo
"r+" -> Usado somente para LER e ESCREVER algo
"a" -> Usado somente para ACRESCENTAR algo
'''

import os

# Escrevando algo no arquivo:
# with open('celulares.txt', 'w') as arquivo:
#     arquivo.write('Celular 1')


# Acrescentando algo no arquivo, utilizando FOR:
# nomes = ['Joao', 'Emilly', 'Lena', 'Gaba']
# with open('nomes.txt', 'a', newline='') as arquivo:
#     for nome in nomes:
#         arquivo.write(nome + os.linesep)


# Lendo algo no arquivo, utilizando FOR:
# with open('nomes.txt', 'r') as arquivo:
#     for linha in arquivo:
#         print(linha)


# with open('nomes.txt', 'r+', newline='') as arquivo:
#     for linha in arquivo:
#         print(linha)
#     arquivo.write(os.linesep + 'Arthur')

"""
​🥇 DESAFIO Manipulação de Arquivos🥇

# Primeiro crie 3 listas

 * Uma lista que contem 5 frutas

 * Uma lista que contem 5 cores

 * Uma lista que contem 5 linguagens de programação

# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas

# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt

# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt

# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.

# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?
"""
'''
frutas = ['Banana', 'Uva', 'Kiwi', 'Pera', 'Abacaxi']
cores = ['Verde', 'Amarelo', 'Vermelho', 'Azul', 'Laranja']

with open('frutas.txt', 'a', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)
        print(fruta)
    for cor in cores:
        arquivo.write(cor + os.linesep)
'''
'''
linguagens = ['Python', 'Java', 'JavaScript', 'Go', 'PHP']

with open('Top_5_Linguagens.txt', 'a', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)
'''

extencoes = ['txt', 'ini']

for extecao in extencoes:
    with open(f'arquivo_bonus.{extecao}', 'a') as arquivo:
        arquivo.write('Teste')
