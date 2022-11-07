import PySimpleGUI as sg
 
def tela_login():
    sg.theme('Black')
    layout=[
        [sg.Text('Bem - vindo Ao Jogo'),sg.Input(key='usuario')],
        [sg.Button('Jogar')]
    ]
    return sg.Window('Tela de Login',layout=layout, finalize = True)
 
def tela_pedido():
    sg.theme('Black')
    layout = [
        [sg.Text('Escolha Pedra, Papel ou Tesoura')],
        [sg.Checkbox('Big Mc', key='pedido1'),sg.Checkbox('Duplo Quarteirão',key='pedido2')],
        [sg.Checkbox('Mc Chicken',key='pedido3'), sg.Checkbox('Cheddar McMelt',key='pedido4')]
    ]
 
    return sg.Window('Tela do pedido', layout=layout, finalize= True)

janela1, janela2 = tela_login(), None
 
while True:
    janela,evento, valores = sg.read_all_windows()
    #fechar janelas
    if janela == janela1  and evento == sg.WINDOW_CLOSED:
        break
    if janela == janela2 and evento == sg.WINDOW_CLOSED:
        break
    if valores['usuario'] == 'gustavinho ak trovao':
        janela2 = tela_pedido()
        janela1.hide()
    else:
        print("Usuario ou senha invalidos")