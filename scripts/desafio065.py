'''Desafio065: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
MAIORIDADE: 24 ANOS'''
#
from datetime import date

maiores = 0
menores = 0

for c in range (0, 7):
  nasc = int(input('Insira seu ano de nascimento: '))
  idade = date.today().year - nasc
  if idade >= 21:
    maiores += 1
  else:
    menores += 1

print(f'Total de pessoas que são maoires de idade (+21 anos): {maiores}.')
print(f'Total de pessoas que não atingiram a maioridade (-21 anos): {menores}.')
