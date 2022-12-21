#Desafio 74: Escreva um programa que leia um número N inteiro e mostre na tela os N primeiros termos de uma sequência de  Fibonacci.
#
n = int(input('Quantos termos da Sequência de Fibonacci gostaria de ver? '))

t1 = 0
t2 = 1

while n != 0:
  print (f'{t1} ->', end =' ')
  t1 += t2
  n -= 1
  if n != 0:
    print (f'{t2} ->', end = ' ')
    t2 += t1
    n -= 1
print('Fim da sequência.')
