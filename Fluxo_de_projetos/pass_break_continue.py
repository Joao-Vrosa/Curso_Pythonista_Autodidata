# pass
# numero = 0
# while numero < 5:
#     pass

# for numero in range(10):
#     pass


# # continue - ignorar/pular
# for numero in range(10):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         continue


# # break - interromper a operacao
# for numero in range(10):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         break
    


## Desafio 1

# Use a operação necessária(break ou continue) para que a seguinte condição aconteça.
# Ao cegar ao estilo "Rap" o mesmo não deve ser impresso na tela
estilos = ['Hip-Hop','Rock','Rap','Pop']

for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(f'-> {estilo}')


## Desafio 2 
# Use a operação necessária(braek ou continue) para que a seguinte condição aconteça:
# Ao chegar ao estilo "Rock" a execução deve interrompida
for estilo in estilos:
    if estilo == 'Rock':
        break
    print(f'-> {estilo}')

