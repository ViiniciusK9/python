import pymysql.cursors 
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        port=3307,
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        print(f'Conexão fechada com sucesso!')
        conexao.close()


def consulta_sql(sql, dados=None, many=False):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = sql
            if many:
                cursor.executemany(sql, dados)
            else:
                cursor.execute(sql, dados)
            conexao.commit()


def consulta_sql_retorno(sql, dados=None):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = sql
            cursor.execute(sql, dados)
            return cursor.fetchall()


def listar_dados(limite):
    sql = f'SELECT * FROM clientes ORDER BY id ASC LIMIT {limite}'
    resultado = consulta_sql_retorno(sql)
    for linha in resultado:
        print(linha)


def inserir_registro(nome, sobrenome, idade, peso):
    sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
    dados = (nome, sobrenome, idade, peso)
    consulta_sql(sql, dados)


def inserir_registros(dados):
    sql = f'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
    consulta_sql(sql, dados, many=True)

    """  Dados precisam ser uma lista de tuplas contendo nome, sobrenome, idade e peso.
    dados = [
        ('Maria', 'Santos', 28, 55.5),
        ('Matheus', 'Santos', 28, 55.5),
        ('Daniel', 'Santos', 28, 55.5),
        ] 
    """


def deletar_registro(id):
    sql = 'DELETE FROM clientes WHERE id = %s'
    consulta_sql(sql, id)


def qnt_elementos(quantidade):
    string = ''
    for i in range(1, (quantidade + 1)):
        if i < quantidade:
            string += '%s, '
        else:
            string += '%s'
    return string


def deletar_registros(ids_deletar):
    qnt = qnt_elementos(len(ids_deletar))
    sql = f'DELETE FROM clientes WHERE id IN ({qnt})'
    consulta_sql(sql, ids_deletar)


def deletar_registros_range(id_inicio, id_fim):
    sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
    consulta_sql(sql, (id_inicio, id_fim))


def atualizar_nome_registro(nome, id):
    sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
    consulta_sql(sql, (nome, id))


# ORDER BY id DESC 
# ORDER BY id ASC
# LIMIT 100
# Seleciona e lista os dados da base de dados

if __name__ == '__main__':
    dados = [
        ('Maria', 'Santos', 28, 55.5),
        ('Matheus', 'Santos', 28, 55.5),
        ('Daniel', 'Santos', 28, 55.5),
    ]
    # inserir_registros(dados)
    # deletar_registro(id=14)
    
    ids_deletar = (
        12, 13, 14, 15, 16, 17, 18
    )
    # deletar_registros(ids_deletar)
    # deletar_registros_range(id_inicio=20, id_fim=25)

    # atualizar_nome_registro(nome='Marcos', id=26)

    listar_dados(100)
