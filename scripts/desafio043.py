'''faça um programa que calcule 2^n onde N é uma informação inserida pelo usuário e deve ser inteiro e positivo. Imprima o resultado do cálculo através de laço de repetição.
OBS: 2° = 1 e 2¹ = 2'''
#
n = int(input('Insira um número (inteiro e posivito apenas): '))
c = 1
pot = 2

if n > 1:
  while c < n:
    pot *= 2
    c += 1
  print(f'O resultado foi {pot}.')
elif n == 0:
  print('O resultado foi 1.')
elif n == 1:
  print(f'O resultado foi {pot}.')
else:
  print('Número inválido, apenas números inteiros e positivos são permitidos.')
