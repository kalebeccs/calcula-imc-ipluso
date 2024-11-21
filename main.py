from db import *
from interface import *
from users import *

lista_users = [
    ('Ana Silva', 28, 1.65, 60.0),
    ('Carlos Souza', 35, 1.75, 80.0),
    ('Mariana Costa', 22, 1.58, 54.0),
    ('João Pereira', 42, 1.82, 90.5),
    ('Lucia Mendes', 30, 1.70, 68.2)
]

criar_tabela_users(conn(), True)

inserir_users(conn(), lista_users)

print_IMC(consulta_por_nome(cursor(), 'Ana Silva'))

# usuario_insere_novos_usuarios(conn())
# usuario_pesquisa_imc(cursor())

close()