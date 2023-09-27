
# split() - Ira quebrar por padrao pelo spaco em branco ou conforme parametro.

frase = 'Ola, eu sou o Joao V Rosa'

print(frase.split())
print(frase.split(','))

nomes = 'Joao, Emilly, Lena, Gaba, Tutu'

print(nomes.split())
print(nomes.split(','))


nomes_separados_por_espaco = nomes.split(' ')

print(nomes_separados_por_espaco)

print(','.join(nomes_separados_por_espaco))
print('.'.join(nomes_separados_por_espaco))
print('-'.join(nomes_separados_por_espaco))
print(' '.join(nomes_separados_por_espaco))
