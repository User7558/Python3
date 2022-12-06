#Desafio 71: Faça um programa que leia um número qualquer e mostre seu fatorial.
#
n = int(input('Digite um número: '))
c = n
fatorial = 1

while n != 0:
  fatorial = fatorial * n
  n -= 1

print(f'Fatorial de {c}: {fatorial}')
