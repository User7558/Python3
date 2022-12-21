#Desafio 76: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor digitado. o programa deve perguntar usuário se ele quer ou não continuar a digitar valores.
#
n = maior = media = c = s = 0
menor = 999999999
r = ''

while r != 'N':
  n = int(input('Digite um valor: '))
  s += n
  c += 1
  if n < menor:
    menor = n
  elif n > maior:
    maior = n
  media = s/c
  r = str(input('Deseja digitar mais números? [S/N]')).upper()

print(f'Menor: {menor}')
print(f'Maior: {maior}')
print(f'Média: {media}')
