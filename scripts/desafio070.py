'''Desafio 70: Crie um programa que leia dois valores e mostre um menu na tela:
  1.somar
  2.maior
  3.multiplicar
  4.novos números
  5. sair do programa'''
#
from time import sleep

menu =''

print('CALCULADORA')
print('='*20)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print(' ')

while menu != 5:
  menu = int(input('''Escolha uma opção:
  [1] Somar
  [2] Multiplicar
  [3] Qual o maior número
  [4] Digitar novos números
  [5] Sair do programa
  ---------------------------
  '''))

  if menu == 1:
    soma = n1+n2
    print(f'A soma entre {n1} e {n2} é igual a {soma}.')
  elif menu == 2:
    mult = n1*n2
    print(f'A multiplicação entre {n1} e {n2} resultou em {mult}.')
  elif menu == 3:
    if n1 > n2:
      print(f'Entre {n1} e {n2}, o maior número é {n1}.')
    else:
      print(f'Entre {n1} e {n2}, o maior número é {n2}.')
  elif menu == 4:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
  elif menu == 5:
    print('Saindo...')
  else:
    print('Resposta invalida, escolha as opções entre 1 e 5.')
  print(' ')
  sleep(1)
