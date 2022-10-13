#Desafio063: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#
tot = 0

n = int(input('Digite um número:'))
for c in range (1,n+1):
  if n%c == 0:
    print('\033[33m', end=' ')
    tot += 1
  else:
    print('\033[34m', end=' ')
  print(c, end=' ')
print(f'\n\033[mO número {n} é divisível por {tot} números.')
if tot==2:
  print(f'Logo, {n} é um número primo.')
else:
  print(f'Logo, {n} não é um número primo.')
