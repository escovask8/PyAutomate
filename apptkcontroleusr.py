import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.scrolledtext import ScrolledText
import json
import os
import shutil

# Caminho do arquivo de usuários
USER_FILE = 'users.json'

# Função para carregar os usuários
def carregar_usuarios():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as file:
            return json.load(file)
    return {}

# Função para salvar os usuários
def salvar_usuarios(usuarios):
    with open(USER_FILE, 'w') as file:
        json.dump(usuarios, file)

# Função para atualizar o log
def atualizar_log(mensagem):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, f'{mensagem}\n')
    log_text.config(state=tk.DISABLED)
    log_text.yview(tk.END)

# Função de registro
def registrar():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    usuarios = carregar_usuarios()
    if usuario in usuarios:
        messagebox.showerror("Erro", "Usuário já registrado!")
    else:
        usuarios[usuario] = senha
        salvar_usuarios(usuarios)
        messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
        abrir_tela_login()

# Função de login
def login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    usuarios = carregar_usuarios()
    if usuario in usuarios and usuarios[usuario] == senha:
        atualizar_log('Login bem-sucedido')
        abrir_tela_principal()
    else:
        atualizar_log('Login falhou. Por favor, tente novamente.')

# Função para abrir a tela de login
def abrir_tela_login():
    tela_registro.withdraw()  # Esconde a tela de registro
    root.deiconify()  # Mostra a tela de login

# Função para abrir a tela de registro
def abrir_tela_registro():
    root.withdraw()  # Esconde a tela de login
    global tela_registro
    tela_registro = tk.Toplevel()
    tela_registro.title('Registro')

    tk.Label(tela_registro, text='Usuário').grid(row=0, column=0)
    global usuario_entry
    usuario_entry = tk.Entry(tela_registro)
    usuario_entry.grid(row=0, column=1)

    tk.Label(tela_registro, text='Senha').grid(row=1, column=0)
    global senha_entry
    senha_entry = tk.Entry(tela_registro, show='*')
    senha_entry.grid(row=1, column=1)

    registrar_button = tk.Button(tela_registro, text='Registrar', command=registrar)
    registrar_button.grid(row=2, columnspan=2)

# Função para abrir a tela principal após o login bem-sucedido
def abrir_tela_principal():
    root.withdraw()  # Esconde a tela de login
    tela_principal = tk.Toplevel()
    tela_principal.title('Tela Principal')

    tk.Label(tela_principal, text='Bem-vindo!').pack()
    tk.Button(tela_principal, text='Selecionar e Mover Arquivo', command=selecionar_arquivo).pack()
    tk.Button(tela_principal, text='Sair', command=tela_principal.destroy).pack()

    tela_principal.protocol("WM_DELETE_WINDOW", on_closing)

# Função para selecionar e mover um arquivo (exemplo de automação)
def selecionar_arquivo():
    filepath = filedialog.askopenfilename()
    if filepath:
        atualizar_log(f'Selecionado arquivo: {filepath}')
        destino = "/caminho/para/pasta/destino"
        if not os.path.exists(destino):
            os.makedirs(destino)
        shutil.move(filepath, os.path.join(destino, os.path.basename(filepath)))
        atualizar_log(f'Arquivo movido para: {destino}')

# Função para fechar a aplicação
def on_closing():
    if messagebox.askokcancel("Sair", "Você quer sair?"):
        root.destroy()

# Cria a janela principal
root = tk.Tk()
root.title('Login')

# Layout da tela de login
tk.Label(root, text='Usuário').grid(row=0, column=0)
usuario_entry = tk.Entry(root)
usuario_entry.grid(row=0, column=1)

tk.Label(root, text='Senha').grid(row=1, column=0)
senha_entry = tk.Entry(root, show='*')
senha_entry.grid(row=1, column=1)

login_button = tk.Button(root, text='Login', command=login)
login_button.grid(row=2, columnspan=2)

registrar_button = tk.Button(root, text='Registrar', command=abrir_tela_registro)
registrar_button.grid(row=3, columnspan=2)

tk.Label(root, text='Log').grid(row=4, columnspan=2)
log_text = ScrolledText(root, width=50, height=10, state=tk.DISABLED)
log_text.grid(row=5, columnspan=2)

# Configura o evento de fechamento da janela
root.protocol("WM_DELETE_WINDOW", on_closing)

# Inicia o loop principal da interface gráfica
root.mainloop()


