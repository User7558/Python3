import PySimpleGUI as sg

#layout
sg.theme('SystemDefault')
layout = [
  [sg.Text('Preencha os campos corretamente para efetuar seu login.')],
  [sg.Text('Usuário: '), sg.Input(key='usuario',size=(30,1))],
  [sg.Text('Senha: '), sg.Input(key='senha', password_char='*', size=(31,1))],
  [sg.Checkbox('Salvar login?', default=False, key='salvar')],
  [sg.Button('Entrar')]
]

#janela
janela = sg.Window('Não sabe a senha? Espie o código...', layout)

#ler eventos
while True:
  eventos, valores = janela.read() #unpacking
  if eventos == sg.WIN_CLOSED:
    break
  if eventos == 'Entrar':
    if valores['usuario'] == 'BeepBoop' and valores['senha'] == '123123':
      print('Login efetuado com sucesso!')
      if valores['salvar'] == True:
        print('Login salvo.')
    if valores['usuario'] != 'BeepBoop' or valores['senha'] != '123123':
      print('Senha ou usuário incorretos, por favor tente novamente.')
