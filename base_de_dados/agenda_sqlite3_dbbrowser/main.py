""" Comando utilizado no BD_BROWSER para criar a tabela.
CREATE TABLE "agenda" (
	"id"	INTEGER,
	"nome"	TEXT,
	"telefone"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conexao.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conexao.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conexao.commit() 

    def listar(self):
        consulta = 'SELECT * FROM agenda'
        self.cursor.execute(consulta)
        
        for linha in self.cursor.fetchall():
            id, nome, peso = linha

            print(f'Id: {id}\nNome: {nome}\nPeso: {peso}\n')

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        
        for linha in self.cursor.fetchall():
            id, nome, peso = linha

            print(f'Id: {id}\nNome: {nome}\nPeso: {peso}\n')

    def fechar(self):
        self.cursor.close()
        self.conexao.close() 


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')