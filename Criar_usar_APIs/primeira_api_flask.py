# Primeira API - Flask

from flask import Flask, jsonify, request, make_response
from estrutura_api_sql import Autor, Postagem, app, db
import json
import jwt
from datetime import datetime, timedelta
from functools import wraps


def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        # Verificar se token foi enviado
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'Menssagem': 'Token nao foi incluido!'}, 401)
        # Se temos um token, validar acesso consultado acesso DB
        try:
            resultado = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            autor = Autor.query.filter_by(id_autor=resultado['id_autor']).first()
        except:
            return jsonify({'Menssagem': 'Token Invalido!'})
        return f(autor, *args, **kwargs)
    return decorated


@app.route('/login')
def login():
    auth = request.authorization
    if not auth or auth.username or auth.password:
        return make_response('Login Invalido', 401, {'WWW-Authenticate':'Basic realm="Login Obrigatorio"'})
    usuario = Autor.query.filter_by(nome=auth.username).first()
    if not usuario:
        return make_response('Login Invalido', 401, {'WWW-Authenticate':'Basic realm="Login Obrigatorio"'})
    if auth.password == usuario.senha:
        token = jwt.encode({'id_autor': usuario.id_autor, 'exp': datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        
        return jsonify({'token': token})
    return make_response('Login Invalido', 401, {'WWW-Authenticate':'Basic realm="Login Obrigatorio"'})


# Rota padrão(Pode ser entendido como GET passando o URL Base http://localhost:5000)
@app.route('/')
@token_obrigatorio
def obter_postagens(autor):
    postagens = Postagem.query.all()
    lista_de_postagens = []
    for postagem in postagens:
        postagem_atual = {}
        postagem_atual['id_postagem'] = postagem.id_postagem
        postagem_atual['titulo'] = postagem.titulo
        postagem_atual['email'] = postagem.email
        lista_de_postagens.append(postagem_atual)
    return jsonify({'postagens': lista_de_postagens})

 
# GET - Obter postagem por Id - GET http://localhost:5000/postagem/1
@app.route('/postagem/<int:id_postagem>', methods=['GET'])
@token_obrigatorio
def obter_postagem_por_indice(autor, id_postagem):
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem:
        return jsonify('Postagem não encontrada!')
    postagem_atual = {}
    postagem_atual['id_postagem'] = postagem.id_postagem
    postagem_atual['titulo'] = postagem.titulo
    postagem_atual['email'] = postagem.email
    return jsonify({'postagem': postagem_atual})

 
# Criar uma nova postagem - POST http://localhost:5000/postagem
@app.route('/postagem', methods=['POST'])
@token_obrigatorio
def nova_postagem(autor):
    nova_postagem = request.get_json()
    postagem = Postagem(titulo=nova_postagem['titulo'], senha=nova_postagem['senha'], email=nova_postagem['email'])
    db.session.add(postagem)
    db.session.commit()
    return jsonify({'mensagem':'Postagem criada com sucesso!'}, 200)

 
# Alterar uma postagem existente - PUT http://localhost:5000/postagem/indice
@app.route('/postagem/<int:id_postagem>', methods=['PUT'])
@token_obrigatorio
def alterar_postagem(autor, id_postagem):
    postagem_alterada = request.get_json()
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem:
        return jsonify({'mensagem':'Esta postagem não foi encontrada.'})
    try:
        if postagem_alterada['titulo']:
            postagem.titulo = postagem_alterada['titulo']
    except:
        pass
    try:
        if postagem_alterada['email']:
            postagem.email = postagem_alterada['email']
    except:
        pass
    try:
        if postagem_alterada['senha']:
            postagem.senha = postagem_alterada['senha']
        db.session.commit()
    except:
        pass
    return jsonify({'mensagem':'Postagem alterada com sucesso!'})

 
# DELETE http://localhost:5000/cancoes/indice
@app.route('/postagem/<int:id_postagem>', methods=['DELETE'])
@token_obrigatorio
def deletar_postagem(autor, id_postagem):
    postagem_existente = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem_existente:
        return jsonify({'mensagem':'Esta postagem não foi encontrada.'})
    db.session.delete(postagem_existente)
    db.session.commit()
    return jsonify({'mensagem':'Postagem excluída com sucesso!'})
    



########## Criando a API autores ##########
@app.route('/autores')
@token_obrigatorio
def obter_autores(autor):
    # Extraindo todos os autores do banco de dados
    autores = Autor.query.all()
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_de_autores.append(autor_atual)
        
    return jsonify({'autores': lista_de_autores})


@app.route('/autores/<int:id_autor>', methods=['GET'])
@token_obrigatorio
def obter_autor_id(autor, id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify(f'Autor nao encontrado')
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor
    autor_atual['nome'] = autor.nome
    autor_atual['email'] = autor.email
    
    return jsonify(f'Voce buscou pelo autor: {autor_atual}')
    

@app.route('/autores', methods=['POST'])
@token_obrigatorio
def novo_autor(autor):
    novo_autor = request.get_json()
    autor = Autor(nome=novo_autor['nome'], senha=novo_autor['senha'], email=novo_autor['email'])
    
    db.session.add(autor)
    db.session.commit()
    
    return jsonify({'menssagem': 'Usuario criado com sucesso!'}, 200)
    

@app.route('/autores/<int:id_autor>', methods=['PUT'])
@token_obrigatorio
def alterar_autor(autor, id_autor):
    usuario_a_alterar = request.get_json()
    Autor.query.filter_by(id_autor=id_autor).first()
    if not Autor:
        return jsonify({'Menssagem': 'Este usuario nao foi encontrado!'})
    try:
        autor.nome = usuario_a_alterar['nome']
    except:
        pass
    try:
        autor.email = usuario_a_alterar['email']
    except:
        pass
    try:
        autor.senha = usuario_a_alterar['senha']
    except:
        pass
        
    db.session.commit()
    return jsonify({'Menssagem': 'Usuario alterado com sucesso!'})
    
    

@app.route('/autores/<int:id_autor>', methods=['DELETE'])
@token_obrigatorio
def excluir_autor(autor, id_autor):
    autor_existente = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor_existente:
        return jsonify({'Menssagem': 'Este autor nao foi enc ontrado!'})
    
    db.session.delete(autor_existente)
    db.session.commit()
    
    return jsonify({'Menssagem': 'Autor excluido com sucesso!'})




app.run(port=5000, host='localhost', debug=True)
