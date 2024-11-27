import sqlite3

# Conexão inicial
try:
    _conn = sqlite3.connect('../db/imc.db')
except sqlite3.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    _conn = None

def conn():
    """
    Retorna a conexão com o banco de dados.
    :return: Connection: Conexão com o banco de dados.
    """
    if _conn:
        return _conn
    else:
        raise ConnectionError("Conexão com o banco de dados não está disponível.")

def close():
    """
    Fecha a conexão com o banco de dados.
    :return: None
    """
    if _conn:
        _conn.close()
    else:
        print("Conexão já estava fechada.")
