for numero in range(1, 22, 2):
    print(f'Carregando...{numero}')


nomes = ['Joao', 'Emilly', 'Arthur']
for nome in nomes:
    print(nome)

# Loop Aninhado
celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'-> {celular} {versao}')

