#desafio30: Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
#
n = int(input('Digite um número: '))
if (n%2 == 0):
    print('{} é um número par'.format(n))
else:
    print('{} é um número ímpar'.format(n))
