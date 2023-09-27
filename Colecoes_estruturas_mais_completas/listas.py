"""
precos = [10, 20, 30, 50, 45]

print(precos[1])
print(precos[0])
print(precos[2])

print(precos[precos.index(45)])

itens = [1, 2, 3, 'Ola', 'Mundo', True, 10.5]


lista_de_noves = [9] * 10
print(lista_de_noves)


lista_de_testes = ['Teste'] * 5
print(lista_de_testes)


faixa_de_numeros = list(range(20))
print(faixa_de_numeros)

############### Desafio ###############
Desafio #1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia e imprima ele na tela

Desafio #2 Usando apenas uma linha de código, crie uma lista de 10 a 131

Desafio #3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2

Desafio #4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos
que você mais usa durante o dia, mas agora dentro de cada item você vai colocar 
uma informação extra, coloque o valor em reais desse objeto também e imprima ele na tela  
"""
# Desafio #1
objetos = ['Caneta', 'Papel', 'Celular']
print(objetos)


# Desafio #2
print(list(range(10, 132)))


#Desafio #3
combinacao = objetos + list(range(10, 132))
print(combinacao)


# Desafio #4
objetos_matriz = [['Caneta', 5], ['Papel', 0.5], ['Celular', 1500]]

for obj in objetos_matriz:
    print(f'{obj[0]} -> R${obj[1]}')

