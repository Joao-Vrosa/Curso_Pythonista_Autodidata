# def dar_boas_vindas():
#     print('Bem-vindo!')
    

# dar_boas_vindas()


# def da_boas_vindas_personalizada(nome):
#     print(f'Bem-vindo(a) {nome}')
    

# da_boas_vindas_personalizada('Joao')


# def apresentar_lugar(lugar='nossa loja'):
#     print(f'Conheca {lugar}')
    

# apresentar_lugar()


########## Desafio ##########

def gerar_nome_completo(nome='sem', sobrenome='nome'):
    print(f'Bem-vindo(a) {nome} {sobrenome}')
    
gerar_nome_completo('Joao', 'Rosa')


# Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o 
# segundo parâmetro é a quantidade, porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o 
# resultado do preço do produto, multiplicado a quantidade escolhida.

def calcular_valores(valor, quantidae=1):
    total = valor * quantidae
    print(f'Valor total: {total}')
    
calcular_valores(10, 2)
