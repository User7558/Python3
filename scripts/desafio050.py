'''Desafio051: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal'''
#
n = int(input('Digite um número inteiro: '))
menu = str(input('''Escolha uma base de conversão para {n}:
[1] Binário
[2] Octal
[3] Hexadecimal
- - - - - - - - - -
R: '''))

if menu == '1':
  n = format(n,"b")
  print(n)
elif menu == '2':
  n = format(n,"o")
  print(n)
else:
  n = format(n,"x")
  print(n)
