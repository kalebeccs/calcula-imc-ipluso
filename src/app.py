from db.db import conn, close
from interface import interface_principal
from users import criar_tabela_users, inserir_users

# Dados de exemplo
lista_users = [
    ('Ana Silva', 28, 1.65, 60.0),
    ('Carlos Souza', 35, 1.75, 80.0),
    ('Mariana Costa', 22, 1.58, 54.0),
    ('João Pereira', 42, 1.82, 90.5),
    ('Lucia Mendes', 30, 1.70, 68.2),
    ('Pedro Barros', 50, 1.75, 85.7),
    ('Paula Carvalho', 33, 1.68, 61.3),
    ('Fernando Gomes', 29, 1.77, 78.5),
    ('Marta Nunes', 37, 1.63, 55.0),
    ('Ricardo Alves', 45, 1.80, 88.6)
]

def main():
    """
    Ponto de entrada principal do programa.
    :return: None
    """
    try:
        criar_tabela_users(conn(), True)
        inserir_users(conn(), lista_users)
        interface_principal(conn())
    finally:
        close()

if __name__ == "__main__":
    main()