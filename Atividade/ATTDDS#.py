import os
import sys
from conexao import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        serie INTEGER NOT NULL,
        faltas DECIMAL NOT NULL DEFAULT 0,
        nota1 DECIMAL DEFAULT 0,
        nota2 DECIMAL DEFAULT 0,
        nota3 DECIMAL DEFAULT 0,
        nota4 DECIMAL DEFAULT 0
    )
""")
conexao.commit()


def cadastroAlunos():
    print('========== CADASTRO DE ALUNO ==========\n')
    nome = str(input('Insira o nome do aluno: '))

    os.system('cls' if os.name == 'nt' else 'clear')

    print('========== CADASTRO DE ALUNO ==========\n')
    print('\n[1] 1º Série   [2] 2º Série   [3] 3º Série')
    serie = int(input('Insira a sua série: '))

    cursor.execute("INSERT INTO alunos (nome, serie) VALUES (?, ?)", (nome, serie))
    conexao.commit()
    print("Aluno cadastrado com sucesso!\n")

def verificaSeIdExiste(id):
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (id,))
    resultado = cursor.fetchone()
    if resultado:
        return True

def removerPorId():
    id_estudante = input("Digite o id do aluno que deseja remover: ")
    if(verificaSeIdExiste(id_estudante)):
        cursor.execute("DELETE FROM alunos WHERE id = ?", (id_estudante,))
        conexao.commit()
        print("Aluno removido com sucesso!\n")
    else:
        print("Este id não existe.")
        removerPorId()

def procurarPorId():
    id = input("Digite o id do aluno que deseja buscar: ")
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (id,))
    resultado = cursor.fetchone()

    if resultado:
        print("\n--- Dados do Aluno ---")
        print(f"ID: {resultado[0]}")
        print(f"Nome: {resultado[1]}")
        print(f"Série: {resultado[2]}")
        print(f"Faltas: {resultado[3]}")
        print(f"Nota 1: {resultado[4]}")
        print(f"Nota 2: {resultado[5]}")
        print(f"Nota 3: {resultado[6]}")
        print(f"Nota 4: {resultado[7]}")
    else:
        print("Aluno não encontrado.")


def procurarPorSerie():
    serie = int(input("Digite a série que deseja buscar: "))
    if serie > 3 or serie < 1:
        print("Série inválida")
    else:
        cursor.execute("SELECT * FROM alunos WHERE serie = ?", (serie,))
        alunos = cursor.fetchall()
        
        if not alunos:
            print("Nenhum aluno encontrado para essa série.")
        else:
            print(f"\n--- Alunos da {serie}ª Série ---")
            for aluno in alunos:
                print(f"\nID: {aluno[0]}")
                print(f"Nome: {aluno[1]}")
                print(f"Série: {aluno[2]}")
                print(f"Faltas: {aluno[3]}")
                print(f"Nota 1: {aluno[4]}")
                print(f"Nota 2: {aluno[5]}")
                print(f"Nota 3: {aluno[6]}")
                print(f"Nota 4: {aluno[7]}")



# O MÉTODO A SEGUIR RETORNA Uma lista contendo [O ID(INT), UMA LISTA DE NOTAS(FLOAT) E O NÚMERO DE FALTAS(INT)]
def cadastroDados():
    notas = []
    id_estudante = int(input("Digite o ID do estudante: "))

    if(verificaSeIdExiste(id_estudante)):
        # Garante que as notas estejam entre 0 e 10
        for i in range(1, 5):
            while True:
                try:
                    nota = float(input(f"Digite a {i}° nota: "))
                    while nota < 0 or nota > 10:
                        print("Nota inválida. Digite uma nota entre 0 e 10.")
                        nota = float(input(f"Digite a {i}° nota: "))
                    notas.append(nota)
                    break
                except ValueError:
                    print("Algo na inserção das notas deu errado, digite um valor válido.")

        # Garante que o número de faltas seja inteiro e não negativo
        while True:
            try:
                faltas = int(input("Digite o número de faltas: "))
                if faltas < 0:
                    print("Número de faltas inválido. Digite um número não negativo.")
                else:
                    break
            except ValueError:
                print("Número de faltas inválido. Não alterado.")

        cursor.execute("""
            UPDATE alunos 
            SET nota1 = ?, nota2 = ?, nota3 = ?, nota4 = ?, faltas = ? 
            WHERE id = ?
        """, (notas[0], notas[1], notas[2], notas[3], faltas, id_estudante))
        conexao.commit()
        print("Dados do aluno atualizados!\n")
    else:
        print("ESTE ID NÃO EXISTE!")
        cadastroDados()


def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar Aluno")
        print("2. Atualizar Dados do Aluno")
        print("3. Remover Aluno")
        print("4. Consultar Dados do Aluno")
        print("5. Dados Gerais")
        print("6. Sair")

        escolha = input("Selecione a ação desejada: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        match escolha:
            case "1":
                cadastroAlunos()
            case "2":
                cadastroDados()
            case "3":
                removerPorId()
            case "4":
                procurarPorId()
            case "5":
                procurarPorSerie()
            case "6":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Saindo do programa...")
                cursor.close()
                conexao.close()
                sys.exit()
            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Selecione uma opção válida\n")

menu()
