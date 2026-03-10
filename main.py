from database import conectar

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    nascimento = input("Nascimento: ")
    cpf = input("CPF: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO alunos (nome, nascimento, cpf) VALUES (%s,%s,%s)"
    valores = (nome, nascimento, cpf)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Aluno cadastrado!")

cadastrar_aluno()
