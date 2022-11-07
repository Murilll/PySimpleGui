import PySimpleGUI as sg
 
#criar layout
 
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
    [sg.Button('Logar')]
 
]
 
#criar janela
 
janela = sg.Window('Tela de login',layout)
 
#ler eventos
 
while True:
    eventos, valores = janela.read()
    #fechar janela
    if eventos == sg.WINDOW_CLOSED:
        break
    if valores['usuario'] == 'flavin do pneu' and valores['senha'] == 'coxinha123':
        print("Bem vindo Flavin do Pneu")
    else:
        print("Usuario ou senha incorretos")
