import sqlite3 

# Conectar/criar a base de dados.
conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# Criar a tabela clientes se ela não existir, com as seguintes colunas: id, nome e peso.
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'nome TEXT,'
            'peso REAL'
            ')')


# Formas de inserir dados na base de dados. 
""" cursor.execute(''INSERT INTO clientes (nome, peso) VALUES ('Vinicius', 55))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Joaozinho', 'peso': 40})
cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Joaozinho', 'peso': 40})
conexao.commit() """

# Atualizar dados na tabela conforme o id do cliente.
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id', {'nome': 'Carlos', 'id': 5})
conexao.commit()

# Deletar um registro da tabela clientes conforme o id.
cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 6})
conexao.commit()

# Selecionar todas as informações da tabela clientes.
cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    id, nome, peso = linha

    print(f'Id: {id}\nNome: {nome}\nPeso: {peso}\n')

# Selecionando colunas (nome, peso) da tabela clientes, onde o peso for maior que 65.
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 65')

for linha in cursor.fetchall():
    nome, peso = linha

    print(f'Nome: {nome}\nPeso: {peso}\n')


cursor.close()
conexao.close()
