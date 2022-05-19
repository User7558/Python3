#desafio16: um programa que leia um número Real e mostre sua porção inteira
#
'''MÉTODO 1
from math import trunc
n=float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n, trunc(n)))'''

# MÉTODO 2
n=float(input('Digite um número: '))
print('O valor {} tem a parte inteira {}.'.format(n, int(n)))
