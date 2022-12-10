#Desafio 71: Faça um programa que leia um número qualquer e mostre seu fatorial.
#
n = int(input('Digite um número: '))
fatorial = 1
print(f'Fatorial de {n} = ', end = '')

while n != 0:
  print(f'{n}', end = '')
  print(' x ' if n > 1 else ' = ', end = '')
  fatorial *= n
  n -= 1

print(fatorial)
