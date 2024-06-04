import tkinter as tk
from tkinter import scrolledtext

# Função para atualizar o log
def atualizar_log(mensagem):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, f'{mensagem}\n')
    log_text.config(state=tk.DISABLED)
    log_text.yview(tk.END)

# Função de login
def login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    atualizar_log('Botão de login pressionado')
    if usuario == 'admin' and senha == 'admin':
        atualizar_log('Login bem-sucedido')
        # Simula algumas etapas de automação
        atualizar_log('Iniciando automação...')
        atualizar_log('Etapa 1: Fazendo algo...')
        atualizar_log('Etapa 2: Fazendo outra coisa...')
        atualizar_log('Automação finalizada')
    else:
        atualizar_log('Login falhou. Por favor, tente novamente.')

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

tk.Label(root, text='Log').grid(row=3, columnspan=2)
log_text = scrolledtext.ScrolledText(root, width=50, height=10, state=tk.DISABLED)
log_text.grid(row=4, columnspan=2)

# Inicia o loop principal da interface gráfica
root.mainloop()
