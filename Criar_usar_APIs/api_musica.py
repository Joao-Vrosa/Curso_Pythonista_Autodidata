from flask import Flask, jsonify, request

app = Flask(__name__)

playlist = [
    {
        'cancao': 'Ana Lua',
        'estilo': 'Reggae'
    },
    
    {
        'cancao': 'Depois do Fim',
        'estilo': 'Rock'
    },
    
    {
        'cancao': 'Outra Noite Que Se Vai',
        'estilo': 'Reggae'
    },
    
    {
        'cancao': 'Ceu Azul',
        'estilo': 'Rock'
    },
    
    {
        'cancao': 'Outro Alguem',
        'estilo': 'Rock'
    },
    
    {
        'cancao': 'Ou Nao',
        'estilo': 'Rock'
    },
    
    {
        'cancao': 'Ponto De Vista',
        'estilo': 'Rock'
    },
    
    {
        'cancao': 'Outra Vida',
        'estilo': 'Reggae'
    }
]


# Rota padrao GET http://localhost:5000
@app.route('/')
def consultar_cancoes():
    return jsonify(playlist)

# Consulta individual GET http://localhost:5000/playlist/inidice
@app.route('/playlist/<int:indice>', methods=['GET'])
def consulta_individual(indice):
    return jsonify(playlist[indice])
    

# Criar uma nova postagem POST http://localhost:5000/playlist
@app.route('/playlist', methods=['POST'])
def adicionando_cancao():
    try:
        cancao = request.get_json()
        playlist.append(cancao)
        return jsonify(f'Cancao {cancao} adicionada com sucesso!', 200)
    except:
        return jsonify('Nao foi possivel adicionar a cacao', 404)


# Alterar uma postagem existente PUT http://localhost:5000/playlist/indice
@app.route('/playlist/<int:indice>', methods=['PUT'])
def alterar_cancao(indice):
    try:
        cancao_alterada = request.get_json()
        playlist[indice].update(cancao_alterada)
        return jsonify(f'Cancao alterada com sucesso para {playlist[indice]}', 200)
    except:
        return jsonify('Nao foi possivel alterar a cancao!', 404)


# Excluir uma postagem DELETE
@app.route('/playlist/<int:indice>', methods=['DELETE'])
def excluir_cancao(indice):
    try:
        if playlist[indice] is not None:
            del playlist[indice]
            return jsonify(f'Cancao {playlist[indice]} exclida com sucesso!', 200)
    except:
        return jsonify('Nao foi possivel realizar a exclusao!', 400)


app.run(port=5000, host='localhost', debug=True) # Executando a aplicação
