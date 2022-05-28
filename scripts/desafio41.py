#desafio41: Crie um sistema de login, onde o usuário precisa digitar Nome e Senha, e então uma verificação seguida de uma mensagem de 'Login efetuado' caso as informações coincidam, e 'Nome ou senha inválidos' caso não.
#
from time import sleep

print('='*50)
print('\033[1m BOAS-VINDAS, VAMOS EFETUAR SEU CADASTRO!\033[m')
print('='*50)
sleep(1)
name = str(input('Crie seu nome de usuário: '))
senha = int(input('Crie sua senha (são permitidos apenas números): '))
sleep(1)
print('\033[0;33m CONFIRMANDO CADASTRO...\033[m')
sleep(2)

#fase de confirmação de dados

print('='*50)
print('\033[1m BOAS-VINDAS NOVAMENTE, POR FAVOR CONFIRME SEUS DADOS\033[m')
print('='*50)
name2 = str(input('Digite seu nome de usuário: '))
senha2 = int(input('Digite sua senha: '))

#testes

if (name == name2 and senha == senha2):
  print(f'\033[0;32m LOGIN EFETUADO, OLÁ {name}!\033[m')
elif (name != name2 and senha == senha2):
  print('\033[0;31m NOME DE USUÁRIO INCORRETO, POR FAVOR TENTE NOVAMENTE!\033[m')
elif (name == name2 and senha != senha2):
  print('\033[0;31m SENHA INCORRETA, POR FAVOR TENTE NOVAMENTE!\033[m')
else:
  print('\033[4;31m USUÁRIO E SENHA INCORRETOS, POR FAVOR TENTE NOVAMENTE!\033[m')
