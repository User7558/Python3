#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. no final, mostre os 10 primeiros termos dessa progressão.
#
pa = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão da P.A.: '))

print(' ')
print('-=' * 25)
print('\033[;49;34mMostrando os termos da Progressão Aritmética...\033[m')

for c in range (0, 10):
  print(pa)
  pa += r
print('Fim do programa.')
