def criar_tabela_users(conn, drop):
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

def inserir_user(conn, nome, idade, altura, peso):
    conn.cursor().execute(
        'INSERT INTO users (nome, idade, altura, peso) VALUES (?, ?, ?, ?)',
        (nome, idade, altura, peso))
    conn.commit()

def inserir_users(conn, lista_users):
    for user in lista_users:
        inserir_user(conn, *user)

def ler_users(cursor):
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

def consulta_por_nome(cursor, nome_pesquisa):
    cursor.execute('SELECT * FROM users WHERE nome = ?', (nome_pesquisa,))
    return cursor.fetchone()

def calcula_IMC(peso, altura):
    return peso / altura ** 2

def classificacao_IMC(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc < 25:
        return 'Peso normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    elif 30 <= imc < 35:
        return 'Obesidade Grau 1'
    elif 35 <= imc < 40:
        return 'Obesidade Grau 2'
    else:
        return 'Obesidade Grau 3'