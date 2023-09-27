from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar data
data_exemplo = datetime(2020, 4, 22)
print(data_exemplo)

data_lancamento = datetime.strptime(input('Lancamento: '), '%d/%m/%Y')
print(data_lancamento)
print(type(data_lancamento))

data_atual = datetime.now()
prazo = data_lancamento - data_atual
print(prazo.days)
print(prazo)
