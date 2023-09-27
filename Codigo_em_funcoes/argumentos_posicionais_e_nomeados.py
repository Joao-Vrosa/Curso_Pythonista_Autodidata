# def exibir_preco(nome_produto, preco):
#     print(f'{nome_produto} esta no valor de {preco}')

# # Argumentos posicionais:
# exibir_preco('Uva', 5.75)

# # Argumentos nomeados:
# exibir_preco(nome_produto='Abacaxi', preco=4.95)
# exibir_preco(preco=4.95, nome_produto='Abacaxi')

def gerar_objeto_personalizado(cor, *,altura, formato):
    print(f'{cor}, {altura}, {formato}')
    

gerar_objeto_personalizado('Azul', altura='1.50m', formato='Triangular')

