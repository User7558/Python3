#Desafio063: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#
from unittest import skip

div = 0
d = 2
n = int(input('Digite um número: '))
if n <= 1:
  print(f'O número {n} inserido não é um número primo.')
else:
  for c in range  (1, n):
    if n%d!=0:
      d += 1
    else:
      if d==n:
        div = 0
      else:
        div += 1
  if div >= 1:
    print(f'O número {n} inserido não é um número primo.')
  else:
    print(f'O número {n} inserido é um número primo.')
