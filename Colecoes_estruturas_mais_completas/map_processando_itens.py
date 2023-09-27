# Como podemos criar listas?

# Criar listas usando Loop's e range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Map
nomes = ['Joao', 'Emilly', 'Gaba', 'Lena']

def aprovar_pessoa(nome):
    return nome + ' APROVADO(A)!'

print(list(map(aprovar_pessoa, nomes)))
