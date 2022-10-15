#Desafio064: Crie um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços.
#
frase = str(input('Insira uma frase para verificarmos se ela é um PALÍNDROMO: ')).strip().lower()
junto = frase.replace(' ','')
inverso = ''

for letra in range (len(junto)-1, -1, -1):
  inverso += junto[letra]

if inverso==junto:
  print(f'A frase {frase} é um palíndromo!')
else:
  print(f'A frase {frase} não é um palíndromo...')
print(f'Frase digitada: {junto}. \nInverso: {inverso}.')

#MÉTODO DE FATIAMENTO
'''
frase = str(input('Insira uma frase para verificarmos se ela é um PALÍNDROMO: ')).strip().lower()
junto = frase.replace(' ','')
inverso = junto[::-1]

if inverso==junto:
  print(f'A frase {frase} é um palíndromo!')
else:
  print(f'A frase {frase} não é um palíndromo...')
print(f'Frase digitada: {junto}. \nInverso: {inverso}.')
'''
