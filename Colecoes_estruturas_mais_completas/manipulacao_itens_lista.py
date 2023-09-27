valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
anos = [2001, 2004, 2021, 2023]

# Add ao final da lista
valores.append(10)
print(valores)

# Unir listas
valores.extend(anos)
print(valores)

nova_lista = valores + anos
print(nova_lista)

# Inserir valor
anos.insert(2, 2020)
print(anos)

# Extrair com base no indice
anos_extraido = anos.pop(2)
print(anos_extraido)

# Remover item
anos.remove(2023)
print(anos)

# Removendo por indice
del anos[2]
print(anos)
del valores[1:5]
print(valores)

# Contando a ocorrencia de um valor
print(valores.count(2001))

# Resetar
valores.clear()
print(valores)


