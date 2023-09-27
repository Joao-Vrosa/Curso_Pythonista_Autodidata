trabalho_concluido = False

if trabalho_concluido == True:
    print('Bora dar uma saida!')
else:
    print('Nao posso sair agora...')
    
    
numeros_de_atrasos = 2

if numeros_de_atrasos >= 3:
    print('Diretoria')
elif numeros_de_atrasos == 2:
    print('Sua segunda falta')
elif numeros_de_atrasos == 1:
    print('Sua primeira falta')
else:
    print('Pode entrar')


velocidade_maxima = 50
sua_velocidade = int(input('Velocidade: '))

if sua_velocidade >= 51 and sua_velocidade <= 60:
    print('Levou multa de 2 pontos')
elif sua_velocidade >= 61 and sua_velocidade < 75:
    print('Levou multa de 3 pontos')
elif sua_velocidade >= 75:
    print('Levou multa de 7 pontos')
else:
    print('Nao foi multado')


tamanho_cabelo = 50
# Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00
if tamanho_cabelo <= 20:
    print('Valor: R$50,00')
# Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
elif tamanho_cabelo >= 21 and tamanho_cabelo <= 30:
    print('Valor: R$70,00')
# Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00
elif tamanho_cabelo >= 31 and tamanho_cabelo <= 50:
    print('Valor: R$100,00')
# Acima de 50cm Favor consultar na recepção
else:
    print('Favor consultar na recepção')
