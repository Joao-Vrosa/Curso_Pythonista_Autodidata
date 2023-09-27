# Valores aleatorios com random

import random


print(random.random()) # Gera um valor de 0.0 a 1.0 pro padrao

# Gera um valor decimal de um valor minimo e valor maximo
print(random.uniform(2, 20))

# Gera um valor inteiro de um valor minimo e valor maximo
print(random.randint(20, 50))

# Gera opcao aleatoria
cores = ['Vermelho', 'Amarelo', 'Azul', 'Verde']
print(random.choices(cores))
print(random.choices(cores, k=2)) # Gera duas opcoes aleatorias, conforme parametro.

# Embaralhando items
cartas = ['carta1', 'carta2', 'carta3', 'carta4']
random.shuffle(cartas)
print(cartas)

# Desafios Random

# 1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
cara_coroa = ['Cara', 'Coroa']
print(random.choice(cara_coroa))

# 2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes
nomes = ['Joao', 'Emilly', 'Lena' , 'Gaba', 'Arthur']
print(random.choice(nomes))

# 3. você quer escolher aleatóriamente um número de 10-100
print(random.randint(10, 100))
