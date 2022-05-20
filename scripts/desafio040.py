'''desafio40: faça um programa de um programa ue determine o MAIOR dentre  400 números inseridos.
  OBS: só é possivel mostrar o maior dos números no FINAL de todas as inserções'''
#
x = 1
z = 1
while (x<=400):
  y = int(input('Insira o número {}: '.format(x)))
  if (y>z):
    z=y
  x = x+1
print('O maior número inserido foi {}'.format(z))
