import PySimpleGUI as sg

# Define o tema da interface
sg.theme('reddit')

# Layout da tela de login
tela_login = [
    [sg.Text('Usuário')],                      # Texto para o campo de usuário
    [sg.Input(key='usuario')],                 # Campo de entrada para o usuário
    [sg.Text('Senha')],                        # Texto para o campo de senha
    [sg.Input(password_char='*', key='senha')],# Campo de entrada para a senha (oculta os caracteres)
    [sg.Button('Login')],                      # Botão de login
    [sg.Text('Log')],                          # Texto para o campo de log
    [sg.Multiline(size=(50, 10), key='log', autoscroll=True, disabled=True)] # Campo de log (multilinha)
]

# Cria a janela
window = sg.Window('Login', tela_login)

# Função para atualizar o log
def atualizar_log(mensagem):
    window['log'].update(f'{mensagem}\n', append=True)

# Loop de eventos
while True:
    event, values = window.read()              # Lê os eventos e valores da janela
    if event == sg.WINDOW_CLOSED:              # Se a janela for fechada, encerra o loop
        break
    if event == 'Login':                       # Se o botão de login for pressionado
        usuario = values['usuario']            # Obtém o valor do campo de usuário
        senha = values['senha']                # Obtém o valor do campo de senha
        # Exemplo de lógica de login (substitua pela sua lógica real de login)
        atualizar_log('Botão de login pressionado')
        if usuario == 'admin' and senha == 'admin': # Verifica se o usuário e a senha estão corretos
            atualizar_log('Login bem-sucedido')
            # Simula algumas etapas de automação
            atualizar_log('Iniciando automação...')
            atualizar_log('Etapa 1: Fazendo algo...')
            atualizar_log('Etapa 2: Fazendo outra coisa...')
            atualizar_log('Automação finalizada')
        else:
            atualizar_log('Login falhou. Por favor, tente novamente.')

window.close()  # Fecha a janela
