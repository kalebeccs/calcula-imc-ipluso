from db.db import *

def main():
    print("Inicializando o banco de dados...")
    initialize_db()  # Cria as tabelas no banco de dados
    print("Banco de dados configurado com sucesso!")

if __name__ == "__main__":
    main()
    close()