import sqlite3

def criar_conexao():
    try:
        conexao = sqlite3.connect("banco.db")  # Cria um arquivo local chamado banco.db
        return conexao
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao SQLite: {e}")
        return None
