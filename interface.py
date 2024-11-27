import customtkinter as ctk
from tkinter import messagebox

from db import *
from users import *

# Configurando o tema do CustomTkinter
ctk.set_appearance_mode("System")  # Modo Claro ou Escuro
ctk.set_default_color_theme("blue") 

def criar_janela():
    janela = ctk.CTk()
    janela.title("Gerenciador de Usuários - IMC")
    janela.geometry("640x480")  # Largura x Altura
    return janela

def interface_principal(conn):
    janela = criar_janela()

    # Título
    titulo = ctk.CTkLabel(janela, text="Bem-vindo ao Sistema de IMC", font=("Arial", 20))
    titulo.pack(pady=20)

    # Botões para ações
    btn_inserir = ctk.CTkButton(janela, text="Inserir Usuário", command=lambda: inserir_usuario_tela(conn))
    btn_inserir.pack(pady=10)

    btn_consultar = ctk.CTkButton(janela, text="Consultar IMC", command=lambda: consultar_imc_tela(conn))
    btn_consultar.pack(pady=10)

    btn_consultar_users = ctk.CTkButton(janela, text="Ver Usuários Cadastrados", command=lambda: consultar_users_tela(conn))
    btn_consultar_users.pack(pady=10)

    btn_sair = ctk.CTkButton(janela, text="Sair", command=janela.quit)
    btn_sair.pack(pady=20)

    janela.mainloop()

def inserir_usuario_tela(conn):
    def salvar_usuario():
        nome = entry_nome.get()
        idade = int(entry_idade.get())
        altura = float(entry_altura.get())
        peso = float(entry_peso.get())

        # Inserir no banco de dados
        inserir_user(conn, nome, idade, altura, peso)
        messagebox.showinfo("Sucesso", f"Usuário {nome} inserido com sucesso!")
        janela_inserir.destroy()

    janela_inserir = ctk.CTkToplevel()
    janela_inserir.title("Inserir Usuário")
    janela_inserir.geometry("640x480")

    ctk.CTkLabel(janela_inserir, text="Nome:").pack()
    entry_nome = ctk.CTkEntry(janela_inserir)
    entry_nome.pack()

    ctk.CTkLabel(janela_inserir, text="Idade:").pack()
    entry_idade = ctk.CTkEntry(janela_inserir)
    entry_idade.pack()

    ctk.CTkLabel(janela_inserir, text="Altura (m):").pack()
    entry_altura = ctk.CTkEntry(janela_inserir)
    entry_altura.pack()

    ctk.CTkLabel(janela_inserir, text="Peso (kg):").pack()
    entry_peso = ctk.CTkEntry(janela_inserir)
    entry_peso.pack()

    ctk.CTkButton(janela_inserir, text="Salvar", command=salvar_usuario).pack(pady=20)

def consultar_imc_tela(conn):
    def consultar():
        nome = entry_nome.get().strip()  # Remove espaços extras
        if not nome:  # Valida se o campo não está vazio
            lbl_resultado.configure(text="Erro: O campo não pode estar vazio!", text_color="red")
            return

        user_data = consulta_por_nome(conn.cursor(), nome)
        if user_data:
            imc = calcula_IMC(user_data[4], user_data[3])
            lbl_resultado.configure(text=f"O IMC de {nome} é: {imc:.1f}", text_color="white")
        else:
            lbl_resultado.configure(text="Erro: Usuário não encontrado!", text_color="red")

    def handle_enter(event):
        consultar()  # Chama a função consultar quando Enter for pressionado

    janela_consultar = ctk.CTkToplevel()
    janela_consultar.title("Consultar IMC")
    janela_consultar.geometry("640x480")

    # Título
    ctk.CTkLabel(janela_consultar, text="Consultar IMC", font=("Arial", 16)).pack(pady=10)

    # Entrada para nome
    ctk.CTkLabel(janela_consultar, text="Nome do usuário:").pack(pady=5)
    entry_nome = ctk.CTkEntry(janela_consultar, width=250)
    entry_nome.pack(pady=5)

    # Vincula a tecla Enter ao campo de entrada
    entry_nome.bind("<Return>", handle_enter)

    # Botão para consultar
    ctk.CTkButton(janela_consultar, text="Consultar", command=consultar).pack(pady=20)

    # Label para exibir o resultado
    lbl_resultado = ctk.CTkLabel(janela_consultar, text="", font=("Arial", 14), anchor="center", width=350)
    lbl_resultado.pack(pady=10)

    # Botão para fechar a janela
    ctk.CTkButton(janela_consultar, text="Fechar", command=janela_consultar.destroy).pack(pady=20)

def consultar_users_tela(conn):
    def mostrar_users():
        users = ler_users(conn.cursor())
        if users:
            for i, user in enumerate(users):
                # Criação de colunas com as informações do usuário
                ctk.CTkLabel(tabela, text=f"{user[0]}", anchor="center", width=50).grid(row=i+1, column=0, padx=5, pady=2)
                ctk.CTkLabel(tabela, text=f"{user[1]}", anchor="w", width=150).grid(row=i+1, column=1, padx=5, pady=2)
                ctk.CTkLabel(tabela, text=f"{user[2]}", anchor="center", width=50).grid(row=i+1, column=2, padx=5, pady=2)
                ctk.CTkLabel(tabela, text=f"{user[3]:.2f}", anchor="center", width=50).grid(row=i+1, column=3, padx=5, pady=2)
                ctk.CTkLabel(tabela, text=f"{user[4]:.2f}", anchor="center", width=50).grid(row=i+1, column=4, padx=5, pady=2)
        else:
            ctk.CTkLabel(tabela, text="Nenhum usuário cadastrado!", anchor="center", font=("Arial", 12)).grid(row=1, column=0, columnspan=5, pady=10)

    # Criar a janela de consulta
    janela_consulta = ctk.CTkToplevel()
    janela_consulta.title("Usuários Cadastrados")
    janela_consulta.geometry("640x480")

    # Título
    titulo = ctk.CTkLabel(janela_consulta, text="Usuários Cadastrados", font=("Arial", 16))
    titulo.pack(pady=20)

    # Frame para tabela
    tabela = ctk.CTkScrollableFrame(janela_consulta, width=580, height=250)
    tabela.pack(pady=10, padx=10)

    # Cabeçalhos da tabela
    ctk.CTkLabel(tabela, text="ID", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=0, padx=5, pady=2)
    ctk.CTkLabel(tabela, text="Nome", font=("Arial", 12, "bold"), anchor="w", width=150).grid(row=0, column=1, padx=5, pady=2)
    ctk.CTkLabel(tabela, text="Idade", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=2, padx=5, pady=2)
    ctk.CTkLabel(tabela, text="Altura (m)", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=3, padx=5, pady=2)
    ctk.CTkLabel(tabela, text="Peso (kg)", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=4, padx=5, pady=2)

    # Preencher a tabela
    mostrar_users()

    # Botão para fechar a janela
    btn_fechar = ctk.CTkButton(janela_consulta, text="Fechar", command=janela_consulta.destroy)
    btn_fechar.pack(pady=20)
