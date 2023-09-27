import json

with open('Colecoes_estruturas_mais_completas/usuarios1.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Convertendo em String
    # print(data['nome'])

with open('Colecoes_estruturas_mais_completas/usuarios2.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Convertendo em String
    # print(data['permissões'])
    
with open('Colecoes_estruturas_mais_completas/usuarios3.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Convertendo em String
    # print(data['usuários'][0]['telefone'])
    
with open('Colecoes_estruturas_mais_completas/usuarios4.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    # print(data['usuários'][0]['permissões'][-1])


########## Desafio ##########

with open('Colecoes_estruturas_mais_completas/desafio.json', encoding='utf-8') as arquivo_desafio:
    data = json.load(arquivo_desafio)
    
    # Imprimir o e-mail do usuário com id 2
    print(data['user'][1]['email'])

    # imprimir a city do usuário com id 1
    print(data['user'][0]['address']['city'])

    # Imprimir o total do pedido do usuário com id 2
    print(data['user'][1]['orders'][0]['total'])
