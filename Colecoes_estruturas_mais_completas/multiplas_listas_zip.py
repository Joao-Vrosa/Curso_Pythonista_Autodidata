a_lista = ['A', 'B', 'C', 'D', 'E']
b_lista = [1, 2, 3, 4, 5]

for a, b in zip(a_lista, b_lista):
    print(a)
    print(b)


produtos = ['PRODUTO 1', 'PRODUTO 2', 'PRODUTO 3']
precos = [150, 200, 350]

for produto, preco in zip(produtos, precos):
    print(f'Salvando produto {produto} com o valor de R${preco}')
