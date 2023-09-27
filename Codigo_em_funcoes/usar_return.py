# Processar VS retornar

# O que é e como usar return:

def exbir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        print(5.47) # Com o print nao e possivel utilizar o valor da funcao

exbir_cotacao_do_dia('usd')


# Como usar:
def exbir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47
    
cotacao = exbir_cotacao_do_dia('usd')

if cotacao > 5:
    print('Investir!')
else:
    print('Nao investir!')

