from datetime import datetime
import random



# 1. Obtenha o nome do usuário
nome_funcionario = str(input('Qual o seu nome? '))

# 2. Obtenha a idade do usuário
idade_funcionario = int(input('Qual a sua idade? '))

# 3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro
data_registro = datetime.now()
formato_brasileiro = "%d/%m/%Y"
registro = data_registro.strftime(formato_brasileiro)

# 4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
# # cartoes = ['R$50,00','R$250,00','R$120,00']
cartoes = ['R$50,00','R$250,00','R$120,00']
sortear_cartao = random.choice(cartoes)

# 5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
aniversario = input('Qual o dia do seu aniversario [DD/MM/AAAA]? ')
data_formatada = datetime.strptime(aniversario, formato_brasileiro)

aniversario_funcionario = data_formatada.strftime(formato_brasileiro)



mensagem = f'\nOlá {nome_funcionario}, seu registro foi concluído com sucesso no dia {registro}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {sortear_cartao}.'
print(mensagem)
