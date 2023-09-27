'''
# Criar listas usando loop - Range
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
'''
# Map
# nomes = ['Joao', 'Emilly', 'Lena', 'Gaba', 'Arthur']
from pprint import pprint


def aprovar_pessoa(nome):
    return nome + ' APROVADO!'


'''
print(list(map(aprovar_pessoa, nomes)))


# Como usar List Compreheension
nova_lista = [2 * i for i in range(10)]
# [expressao for membro in iteravel]
print(nova_lista)

nomes = ['Joao', 'Emilly', 'Lena', 'Gaba', 'Arthur']
print([nome + ' APROVADO' for nome in nomes])
'''
##

pprint([[i for i in range(1, 6)] for x in range(5)])

##

nomes = ['Joao', 'Emilly', 'Lena', 'Gaba', 'Arthur']

print([aprovar_pessoa(nome) for nome in nomes if nome != 'Joao'])
# [expressao for membro in iteravel (condicional if)]

# Valores numericos
def numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False
    
    
print([i for i in range(21) if numero_par(i)])

# A condicional e flexivel
# [expressao (condicional if) for membro in iteravel ]
participantes = ['Joao', 'Emilly', 'Lena', 'Gaba', 'Arthur']
ganhadores = ['Joao', 'Emilly']
print([i + ' GANHADOR' if i in ganhadores else i + ' NAO SELECIONADO' for i in participantes])
