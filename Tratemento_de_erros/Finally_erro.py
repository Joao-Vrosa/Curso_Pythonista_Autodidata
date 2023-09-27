internet = None

try:
    print('Fazendo conexao com a ' + internet)
except TypeError as erro:
    print('Nao ha conexao com a internet')
finally:
    print('Desfazendo a compra!')

try:
    valor = int(input('Valor: '))
    print(valor / 0)
except ZeroDivisionError as erro:
    print('Nao e possivel dividir por zero!')
except ValueError as erro:
    print('Favor, digitar apenas numeros!')
finally:
    print('A operacao foi cancelada!')
