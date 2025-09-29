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

def menu():
    print ("--- Menu ---")
    print("1. Cadastrar Aluno")
    print("2. Atualizar Dados do Aluno")
    print("3. Remover Aluno")
    print("4. Consultar Dados do Aluno")
    print("5. Dados Gerais")
    print("6. Sair")
    
    escolha=input ("Selecione a ação desejada: ")
    
    match escolha:
        case "1":
            cadastroAlunos()
        case "2":
            Atualizar_dados()
        case "3":
            removerPorId()
        case "4":
            procurarPorId()
        case "5":
            dados_gerais()
        case "6":
            os.system('cls')
            print ("Saindo do programa...")
            sys.exit()
        case _:
            os.system('cls')
            print("Selecione uma opção válida\n")
            menu()
menu()     


def cadastroAlunos(nome, serie):
    print('==========CADASTRO DE ALUNO==========\n')
    nome = str(input('Insira o nome do aluno:'))

    os.system('cls')

    print('==========CADASTRO DE ALUNO==========\n')
    print('\n[1] 1º Série   [2] 2º Série   [3] 3º Série')
    serie = int(input('Insira a sua série: '))
    '''XXXXXXX(nome, serie)'''
    cursor.execute("INSERT INTO usuarios (nome, serie) VALUES (?, ?)", (nome, serie))

def removerPorId():
    id = input("Digite o id do aluno que deseja remover: ")
    
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id))
    
def procurarPorId():
    id = input("Digite o id do aluno que deseja buscar: ")

    cursor.execute("SELECT * FROM alunos WHERE id = ?", (id))
    for linha in cursor.fetchall():
            print(linha)

def procurarPorSerie():
    serie = input("Digite a serie que deseja buscar: ")
    if serie > 3 or serie < 1:
         print("Serie invalida")
         menu()
    else:
         cursor.execute("SELECT * FROM alunos WHERE serie = ?", (serie))
         for linha in cursor.fetchall():
            print(linha)

#O MÉTODO A SEGUIR RETORNA Uma lista contendo [O ID(INT), UMA LISTA DE NOTAS(FLOAT) E O NÚMERO DE FALTAS(INT)]
def cadastroDados():
    notas = []
    id_estudante = int(input("Digite o ID do estudante: "))

    #GARANTE QUE AS NOTAS ESTEJAM ENTRE 0 E 10
    for i in range(1,4):
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

    #GARANTE QUE O NÚMERO DE FALTAS SEJA INTEIRO E NÃO NEGATIVO
    while True:
        try:
            faltas = int(input("Digite o número de faltas: "))
            if faltas < 0:
                print("Número de faltas inválido. Digite um número não negativo.")
            else:
                break
        except ValueError:
            print("Número de faltas inválido. Não alterado.")

    return cursor.execute("UPDATE usuarios SET nota1 = ?, nota2 = ?, nota3 = ?, nota4 = ?, faltas = ? WHERE id = ?", (nota[0], nota[1],nota[2],nota[3], faltas, id_estudante))

cursor.close()
conexao.close()


