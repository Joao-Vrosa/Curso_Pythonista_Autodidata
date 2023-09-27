# SQlite3
import sqlite3

# Conectar-se ou criar um banco de dados
def conectar_db(nome_db):
    conexao = sqlite3.connect(nome_db)
    return conexao

# Criar tabela
def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Funcionarios (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                cargo TEXT NOT NULL,
                dataContratacao TEXT NOT NULL
            );
    ''')
    conexao.commit() # Salvando

# Inserir dados em uma tabela
def inserir_funcionario(conexao, id, nome, cargo, dataContratacao):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)", (id, nome, cargo, dataContratacao))
    conexao.commit()

# Listar todos os dados de uma tabela
def selecionar_todos_funcionarios(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Funcionarios")
    return cursor.fetchall()

# Alterar dados de uma tabela
def atualizar_funcionario(conexao, id, cargo):
    cursor = conexao.cursor()
    cursor.execute("UPDATE Funcionarios SET cargo = ? WHERE id = ?", (cargo, id))
    conexao.commit()

# Excluir dados de uma tabela
def deletar_funcionario(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Funcionarios WHERE id = ?", (1,)) # Deve ser finalizado com uma virgula caso possua apenas um item
    conexao.commit()


## USANDO AS FUNCOES ##

conexao = conectar_db('Funcionarios.db')

# Criar tabela
criar_tabela(conexao)

# Receber dados do usuario e inserir na aplicacao
nome = input('Nome: ')
cargo = input('Cargo: ')
dataContratacao = input('Data de contracao (aaaa-mm-dd): ')

inserir_funcionario(conexao, 10, nome, cargo, dataContratacao)
inserir_funcionario(conexao, 11, nome, cargo, dataContratacao)

# Pesquisa e retorna os dados da tabela
print(selecionar_todos_funcionarios(conexao)) # Immprime todos os funcionarios

# Alterar os dados da tabela
atualizar_funcionario(conexao, 10, 'Desenvolvedor Python Pleno')

# Excluir um usuario
deletar_funcionario(conexao, 11)

print(selecionar_todos_funcionarios(conexao)) # Imprimindo os funcionarios apos a atualizacao

# Obrigatorio, no caso do SQlite, fechar a conexao, apos fionalizar a operacao
conexao.close()