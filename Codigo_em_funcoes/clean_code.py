from turtle import Turtle

# Crie uma nova turtle
t = Turtle()
# Definir velocidade
t.speed(1)

def pixels_movimento_turtle():
    resposta = int(input('Quanto a tartaruga deve se movimentar? '))
    return resposta

def movimentar():
    resposta = str(input('A tartaruga deve se movimentar para frente(f) ou para trás(t)? ')).upper()
    return resposta

def rotacionar():
    resposta = str(input('A tartaruga deve retacionar para a esquerda(e) ou para a direita(d): ')).upper()
    return resposta

def pixels_rotacao_turtle():
    resposta = int(input('Quanto a tartaruga deve se rotacionar? '))
    return resposta

# Coloca seu programa em loop
while True:
    # Faça perguntas ao usuário para decidir se a tartaruga deve movimentar para frente ou para trás
    movimento = movimentar()
    while movimento not in 'FT':
        print('[ERRO] Opcao invalida, tente novamente!', end=' ')
        movimento = movimentar()
    # Após decidir se ele deve movimentar para frente ou para trás, receba do usuário quantos pixels devem ser percorridos
    if 'F' in movimento:
        movimento_frente = pixels_movimento_turtle()
        t.forward(movimento_frente)
    elif 'T' in movimento:
        movimento_tras = pixels_movimento_turtle()
        t.backward(movimento_tras)

    # Faça perguntas ao usuário para decidir se a tartaruga deve rotacionar para esquerda ou direta
    rotacionar = rotacionar()
    while rotacionar not in 'ED':
        print('[ERRO] Opcao invalida, tente novamente!', end=' ')
        rotacionar = rotacionar()
    # Após decidir se ele deve rotacionar para esquerda ou direita, receba do usuário quantos pixels devem ser rotacionados
    if 'E' in rotacionar:
        rotacionar_esquerda = pixels_rotacao_turtle()
        t.left(rotacionar_esquerda)
    elif 'D' in rotacionar:
        rotacionar_direita = pixels_rotacao_turtle()
        t.right(rotacionar_direita)

    # Ao executar essa ação pergunte ao usuário "Continuar andando?", e reaga de acordo com a resposta do usuário.
    continuar = str(input('-> Deseja continuar andando [S/N]? ')).upper()
    while continuar not in 'SN':
        print('[ERRO] Opcao invalida, tente novamente!', end=' ')
        continuar = str(input('-> Deseja continuar andando [S/N]? ')).upper()
    if continuar in 'N':
        print('<< Obrigado por jogar, volte sempre! >>')
        break

