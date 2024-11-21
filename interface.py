from users import *

def print_IMC(usuario):
    print(f'\nO usuario: {usuario[1]} tem IMC = {round(calcula_IMC(usuario), 1)}')

def usuario_pesquisa_imc(cursor):
    nome_pesquisar = input('Insira um nome para saber o IMC: ')
    print_IMC(consulta_por_nome(cursor, nome_pesquisar))

def usuario_insere_novos_usuarios(conn):
    num_users = int(input('Informe quantos usuarios deseja cadastrar: '))
    for num in range(num_users):
        print(f'\nInserindo dados para o usuario: {num+1}')
        nome = input('Insira um nome: ')
        idade = int(input('Insira a idade: '))
        altura = float(input('Insira a altura: '))
        peso = float(input('Insira o peso: '))
        inserir_user(conn, nome, idade, altura, peso)
