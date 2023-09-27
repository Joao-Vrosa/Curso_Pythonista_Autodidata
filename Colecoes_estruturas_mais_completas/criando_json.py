import json

# Criar ou ler arquivo JSON
computador_json = """{
    "marca": "Dell",
    "preco": 15000
}"""

# Lendo uma string json
data = json.loads(computador_json)
print(data['preco'])

# Salvar uma string json -> arquivo json
with open('computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json)
    
# Lendo o arquivo json
with open('Colecoes_estruturas_mais_completas/computador.json', encoding='utf-8') as arquivo_json:
    str_computador_json = json.load(arquivo_json) # Convertendo JSON -> String
    dicionario_computador_json = json.loads(str_computador_json) # Converter de String -> dicionario Python
    print(dicionario_computador_json['marca'])


####### Desafio #######

pessoa = """{
    "nome": "Joao",
    "idade": 22,
    "cidade": 'Florianopolis',
    "estudante": true,
    "gpa": 3.5
}"""

with open('pessoa_desafio.json', 'w', encoding='utf-8') as arquivo_desafio_json:
    json.dump(pessoa, arquivo_desafio_json)
