#desafio048: Faça um programa que leia um valor em caracteres e exiba a mensagem "senha correta" caso o valor digitado seja igual a "Limão", se o valor digitado for diferente exiba a mensagem "Tente novamente", o programa deve ficar exibindo a mensagem indefinidamente até o usuário acertar a senha correta.
#
s = ''
while s != 'Limão':
  s = str(input('Digite sua senha: '))
  if s != 'Limão':
    print('\033[;31mTente novamente\033[m')
print('\033[;32mSenha correta\033[m')
