# SQL - Structured Query Language (Linguagem Estruturada de Busca)
#  Banco de dados do python, que vem instalado de forma nativa: db.sqlite3

import sqlite3

# Abrir conexao ou criar caso nao exista:
with sqlite3.connect('artistas.db') as conexao:
    # Criar conexao com banco de dados
    sql = conexao.cursor()
    # Rodar comando SQL
    sql.execute('create table banda(nome text, estilo text, membros interger);')
    # Exemplo de inserir dados
    sql.execute('insert into banda(nome, estilo, membros) values ("Lagum", "Rock", 4)')
    # Exemplo de usar dados da minha aplicacao em um comando SQL
    nome = input('Nome da banda: ')
    estilo = input('Estilo da banda: ')
    qtd_integrantes = int(input('Quantidade de integrantes: '))
    
    sql.execute('insert into banda values(?,?,?)', [nome, estilo, qtd_integrantes])
    conexao.commit() # Sempre que precisar que algo seja salvo, utilizar este comando
    
    # Exibir dados no console Python(terminal)
    bandas = sql.execute('select * from banda;')
    for banda in bandas:
        print(banda)
