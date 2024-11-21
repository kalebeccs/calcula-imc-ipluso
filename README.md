# Sistema de Gerenciamento de Usuários com Cálculo de IMC

Este projeto é uma aplicação simples em Python que gerencia usuários, realiza cálculos do Índice de Massa Corporal (IMC) e utiliza **SQLite** como banco de dados. Ele inclui uma interface interativa para que usuários possam inserir dados e consultar informações diretamente do banco.

## Funcionalidades

- **Criação de Tabela:** Cria ou reseta a tabela `users` no banco de dados.
- **Inserção de Usuários:** Insere uma lista inicial de usuários ou novos usuários fornecidos pelo usuário.
- **Consulta de Dados:** Permite pesquisar usuários pelo nome e calcular seu IMC.
- **Interface Interativa (opcional):** Possui funções que permitem a interação do usuário para adicionar novos registros e realizar consultas.

## Estrutura do Projeto

- **`main.py`**: Arquivo principal que executa as operações do sistema.
- **`db.py`**: Contém funções para gerenciar o banco de dados SQLite, como criação de tabelas e conexões.
- **`interface.py`**: Implementa funções interativas para inserção de novos usuários e consulta de IMC.
- **`users.py`**: Define funções relacionadas ao gerenciamento de usuários, como inserção, consulta e cálculo do IMC.

## Pré-requisitos

- **Python 3.x**
- **SQLite** (biblioteca inclusa no Python)

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   cd seuprojeto
   ```

2. Execute o script principal:
   ```bash
   python main.py
   ```

3. Interaja com o sistema conforme necessário. Você pode ativar as funções interativas editando as chamadas comentadas no `main.py`:
   ```python
   usuario_insere_novos_usuarios(conn())
   usuario_pesquisa_imc(cursor())
   ```

## Exemplos de Uso

1. O programa inicializa criando ou limpando a tabela `users` no banco de dados.
2. Insere uma lista de usuários pré-definidos:
   - Ana Silva
   - Carlos Souza
   - Mariana Costa
   - João Pereira
   - Lucia Mendes
3. Calcula e exibe o IMC de **Ana Silva**.

## Estrutura da Tabela `users`

| Campo   | Tipo      | Descrição              |
|---------|-----------|------------------------|
| `nome`  | TEXT      | Nome do usuário        |
| `idade` | INTEGER   | Idade do usuário       |
| `altura`| REAL      | Altura do usuário (m)  |
| `peso`  | REAL      | Peso do usuário (kg)   |

## Funções Disponíveis

### Banco de Dados (`db.py`)
- `criar_tabela_users(conexao, reset=False)`: Cria a tabela de usuários. Use `reset=True` para apagar os dados existentes.
- `conn()`: Retorna uma conexão com o banco de dados.
- `cursor()`: Retorna um cursor para executar comandos SQL.
- `close()`: Fecha a conexão com o banco de dados.

### Gerenciamento de Usuários (`users.py`)
- `inserir_users(conexao, lista)`: Insere uma lista de usuários no banco.
- `consulta_por_nome(cursor, nome)`: Consulta os dados de um usuário pelo nome.
- `print_IMC(user_data)`: Calcula e exibe o IMC de um usuário.

### Interface Interativa (`interface.py`)
- `usuario_insere_novos_usuarios(conexao)`: Permite ao usuário inserir novos usuários via terminal.
- `usuario_pesquisa_imc(cursor)`: Permite ao usuário consultar o IMC de um registro pelo nome via terminal.
