# calcula IMC

Este projeto é um sistema simples de gerenciamento de usuários utilizando **Python** e **SQLite**. Ele permite criar uma tabela de usuários, inserir dados e realizar consultas específicas, como calcular o IMC de um usuário.

## Funcionalidades

- **Criação de Tabela**: Cria a tabela `users` no banco de dados SQLite.
- **Inserção de Dados**: Adiciona múltiplos usuários à tabela.
- **Consulta de Usuários**: Permite buscar usuários pelo nome.
- **Cálculo de IMC**: Calcula e exibe o Índice de Massa Corporal (IMC) de um usuário específico.

## Estrutura do Projeto

- **`main.py`**: Arquivo principal que coordena as operações do sistema.
- **`db.py`**: Contém funções para manipulação do banco de dados, como criação de tabelas e conexões.
- **`users.py`**: Define funções relacionadas aos usuários, como inserção, consulta e cálculo do IMC.

## Pré-requisitos

- Python 3.x instalado.
- Biblioteca SQLite3 (inclusa no Python).

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/projeto-gerenciador-usuarios.git
   cd projeto-gerenciador-usuarios
   ```

2. Instale as dependências, se necessário (opcional).

3. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```

## Exemplos de Uso

Ao executar o programa, ele:

1. Cria uma tabela chamada `users` no banco de dados.
2. Insere os seguintes usuários:
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

## Explicação do Código Principal (`main.py`)

- **`criar_tabela_users(conn())`**: Cria a tabela `users` caso não exista.
- **`inserir_users(conn(), lista_users)`**: Insere uma lista de usuários no banco.
- **`consulta_por_nome(cursor(), 'Ana Silva')`**: Consulta os dados de um usuário pelo nome.
- **`print_IMC(...)`**: Calcula e exibe o IMC do usuário.
