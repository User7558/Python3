'''Desafio051: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal'''
#
n = int(input('Digite um número inteiro: '))
menu = str(input('''Escolha uma base de conversão para {n}:
\033[1;94m[1]\033[m Binário
\033[1;94m[2]\033[m Octal
\033[1;94m[3]\033[m Hexadecimal
\033[1;35m- - - - - - - - - -\033[m
R: '''))

if menu == '1':
  n = format(n,"b")
  print(n)
elif menu == '2':
  n = format(n,"o")
  print(n)
elif menu == '3':
  n = format(n,"x")
  print(n)
else:
  print('\033[90mPor favor, escolha uma opção entre 1 e 3.\033[m')
