import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cadastro_alunos"
    )
    return conexao
