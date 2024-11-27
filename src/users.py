import sqlite3

def criar_tabela_users(conn:sqlite3.Connection, drop=False):
    """
    Cria a tabela 'users' no banco de dados.
    :param conn: Conexão com o banco de dados.
    :param drop: Indica se a tabela existente deve ser descartada antes de criar uma nova.
    :return: None
    """
    if drop:
        conn.cursor().execute('DROP TABLE IF EXISTS users')
    conn.cursor().execute('''
        CREATE TABLE IF NOT EXISTS users (
        pk_user INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        altura REAL NOT NULL,
        peso REAL NOT NULL
        )
    ''')
    conn.commit()

def inserir_user(conn:sqlite3.Connection, nome:str, idade:int, altura:float, peso:float):
    """
    Insere um novo usuário na tabela 'users'.
    :param conn: Conexão com o banco de dados.
    :param nome: Nome do usuário.
    :param idade: Idade do usuário.
    :param altura: Altura do usuário em metros.
    :param peso: Peso do usuário em quilogramas.
    :return: None
    """
    conn.cursor().execute(
        'INSERT INTO users (nome, idade, altura, peso) VALUES (?, ?, ?, ?)',
        (nome, idade, altura, peso))
    conn.commit()

def inserir_users(conn:sqlite3.Connection, lista_users:tuple):
    """
    Insere múltiplos usuários na tabela 'users'.
    :param conn: Conexão com o banco de dados.
    :param lista_users: Lista de usuários (nome, idade, altura, peso).
    :return: None
    """
    for user in lista_users:
        inserir_user(conn, *user)

def ler_users(cursor:sqlite3.Cursor):
    """
    Lê todos os usuários cadastrados na tabela 'users'.
    :param cursor: Cursor do banco de dados.
    :return: Lista de usuários.
    """
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

def consulta_por_nome(cursor:sqlite3.Cursor, nome_pesquisa: str):
    """
    Consulta um usuário pelo nome na tabela 'users'.
    :param cursor: Cursor do banco de dados.
    :param nome_pesquisa: Nome do usuário a ser pesquisado.
    :return: Dados do usuário encontrado ou None.
    """
    cursor.execute('SELECT * FROM users WHERE nome = ?', (nome_pesquisa,))
    return cursor.fetchone()
