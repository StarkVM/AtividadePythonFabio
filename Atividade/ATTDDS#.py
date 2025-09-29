import os
import sys
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
            cadastroDados()
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

def removerPorId():
    id = input("Digite o id do aluno que deseja remover: ")
    
    """XXXXXXX(id)"""
    
def procurarPorId():
    id = input("Digite o id do aluno que deseja buscar: ")

    """XXXXXXX(id)"""

def procurarPorSerie
    serie = input("Digite a serie que deseja buscar: ")
    if serie > 3 or serie < 1:
         print("Serie invalida")
         menu()
    else:
         '''XXXXX(serie)'''

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

    return id_estudante, notas, faltas
