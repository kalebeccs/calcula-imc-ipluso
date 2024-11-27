import customtkinter as ctk

from users import *
from utils import *

# Configurando o tema do CustomTkinter
ctk.set_appearance_mode("System")  # Modo Claro ou Escuro
ctk.set_default_color_theme("blue") 

def criar_janela():
    """
    Cria e configura a janela principal da aplicação.
    Retorna:
    ctk.CTk: A janela principal configurada.
    """
    janela = ctk.CTk()
    janela.title("Gerenciador de Usuários - IMC")  # Define o título da janela
    janela.geometry("640x610")  # Define o tamanho da janela (Largura x Altura)
    return janela

def interface_principal(conn):
    """
    Cria e exibe a interface principal do sistema de IMC.
    Parâmetros:
    conn (sqlite3.Connection): Conexão com o banco de dados SQLite.
    A interface principal inclui:
    - Um título de boas-vindas.
    - Uma tabela de usuários.
    - Uma opção para consultar o IMC dos usuários.
    - Um botão para inserir novos usuários.
    - Um botão para sair da aplicação.
    """
    janela = criar_janela()

    titulo = ctk.CTkLabel(janela, text="Bem-vindo ao Sistema de IMC", font=("Arial", 20))
    titulo.pack(pady=10)

    tabela_usuarios(conn, janela)

    consultar_imc(conn, janela)

    btn_inserir = ctk.CTkButton(janela, text="Inserir Usuário", command=lambda: inserir_usuario(conn, janela))
    btn_inserir.pack(pady=10)

    btn_sair = ctk.CTkButton(janela, text="Sair", command=janela.destroy)
    btn_sair.pack(pady=10)

    janela.mainloop()

def tabela_usuarios(conn, janela):
    # Cabeçalhos da tabela
    frame_cabecalho = ctk.CTkFrame(janela, width=350, height=30)
    frame_cabecalho.pack(pady=(10, 0), padx=10)
    ctk.CTkLabel(frame_cabecalho, text="Nome", font=("Arial", 12, "bold"), anchor="w", width=140).grid(row=0, column=1, padx=(10,5), pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Idade", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=2, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Altura (m)", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=3, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Peso (kg)", font=("Arial", 12, "bold"), anchor="center", width=82).grid(row=0, column=4, padx=5, pady=2)

    # Frame para a tabela de usuários
    frame_tabela = ctk.CTkScrollableFrame(janela, width=350, height=250)
    frame_tabela.pack(pady=(0, 10), padx=10)

    # Carrega usuários na tabela
    users = ler_users(conn.cursor())
    if users:
        for i, user in enumerate(users):
            # Adiciona os dados dos usuários na tabela
            ctk.CTkLabel(frame_tabela, text=f"{user[1]}", anchor="w", width=150).grid(row=i+1, column=1, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{user[2]}", anchor="w", width=50).grid(row=i+1, column=2, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{user[3]:.2f}", anchor="center", width=50).grid(row=i+1, column=3, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{user[4]:.2f}", anchor="center", width=50).grid(row=i+1, column=4, padx=5, pady=2)
    else:
        # Exibe mensagem caso não haja usuários cadastrados
        ctk.CTkLabel(frame_tabela, text="Nenhum usuário cadastrado!", font=("Arial", 12), anchor="center").grid(row=1, column=0, columnspan=5, pady=10)


def consultar_imc(conn, janela):
    def consultar():
        nome = entry_nome.get().strip()  # Remove espaços extras
        if not nome:  # Valida se o campo não está vazio
            lbl_resultado.configure(text="Erro: O campo não pode estar vazio!", text_color="gray")
            return

        user_data = consulta_por_nome(conn.cursor(), nome)
        if user_data:
            imc = calcula_IMC(user_data[4], user_data[3])
            lbl_resultado.configure(text=f"O IMC de {nome} é: {imc:.1f} ({classifica_IMC(imc)})", text_color="white")
            entry_nome.delete(0, "end")  # Limpa o campo de entrada
        else:
            lbl_resultado.configure(text="Erro: Usuário não encontrado!", text_color="gray")

    def handle_enter(event):
        consultar()  # Chama a função consultar quando Enter for pressionado

    # Frame para a consulta de IMC
    frame_consulta = ctk.CTkFrame(janela, width=350, height=100)
    frame_consulta.pack(pady=10, padx=10)

    # Entrada para nome
    titulo = ctk.CTkLabel(frame_consulta, text="Digite um nome para consultar", font=("Arial", 14))
    titulo.grid(row=0, column=0, columnspan=2, pady=5)

    entry_nome = ctk.CTkEntry(frame_consulta, width=220)
    entry_nome.grid(row=1, column=0, padx=(35,10), pady=5)

    # Vincula a tecla Enter ao campo de entrada
    entry_nome.bind("<Return>", handle_enter)

    # Botão para consultar
    ctk.CTkButton(frame_consulta, text="Consultar", command=consultar, width=70).grid(row=1, column=1, padx=(0,35))

    # Label para exibir o resultado
    lbl_resultado = ctk.CTkLabel(frame_consulta, text="", font=("Arial", 14), anchor="center", width=350)
    lbl_resultado.grid(row=2, column=0, columnspan=2, pady=10)

def inserir_usuario(conn, janela):
    def salvar_usuario():
        nome = entry_nome.get()
        idade = int(entry_idade.get()) if entry_idade.get() else None
        altura = float(entry_altura.get()) if entry_altura.get() else None
        peso = float(entry_peso.get()) if entry_peso.get() else None

        if not nome or not idade or not altura or not peso:
            lbl_resultado.configure(text="Erro: Preencha todos os campos!", text_color="gray")
            return

        # Limpar campos
        entry_nome.delete(0, "end")
        entry_idade.delete(0, "end")
        entry_altura.delete(0, "end")
        entry_peso.delete(0, "end")

        # Focus no campo de nome
        entry_nome.focus()

        # Inserir no banco de dados
        inserir_user(conn, nome, idade, altura, peso)

        # Atualizar a mensagem de status
        lbl_resultado.configure(text=f"Usuário {nome} inserido com sucesso!", text_color="white")
        # Limpar mensagem de status após 5 segundos
        janela.after(5000, lambda: lbl_resultado.configure(text=""))

    # Limpar a janela principal
    for widget in janela.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(janela, text="Cadastro de usuarios", font=("Arial", 20))
    titulo.pack(pady=10)

    ctk.CTkLabel(janela, text="Nome:").pack()
    entry_nome = ctk.CTkEntry(janela)
    entry_nome.pack()

    ctk.CTkLabel(janela, text="Idade:").pack()
    entry_idade = ctk.CTkEntry(janela)
    entry_idade.pack()

    ctk.CTkLabel(janela, text="Altura (m):").pack()
    entry_altura = ctk.CTkEntry(janela)
    entry_altura.pack()

    ctk.CTkLabel(janela, text="Peso (kg):").pack()
    entry_peso = ctk.CTkEntry(janela)
    entry_peso.pack()

    ctk.CTkButton(janela, text="Cadastrar", command=salvar_usuario).pack(pady=(20, 10))

    btn_sair = ctk.CTkButton(janela, text="Voltar", command=lambda: carregar_interface_principal(conn, janela))
    btn_sair.pack(pady=10)

    # Label para exibir o status
    lbl_resultado = ctk.CTkLabel(janela, text="", font=("Arial", 14), anchor="center", width=350)
    lbl_resultado.pack(pady=10)

def carregar_interface_principal(conn, janela):
    for widget in janela.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(janela, text="Bem-vindo ao Sistema de IMC", font=("Arial", 20))
    titulo.pack(pady=10)

    tabela_usuarios(conn, janela)

    consultar_imc(conn, janela)

    btn_inserir = ctk.CTkButton(janela, text="Inserir Usuário", command=lambda: inserir_usuario(conn, janela))
    btn_inserir.pack(pady=10)

    btn_sair = ctk.CTkButton(janela, text="Sair", command=janela.destroy)
    btn_sair.pack(pady=10)

    janela.mainloop()
