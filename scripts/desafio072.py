#Desafio 72: Refaça o DESAFIO 62, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
#
pa = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão da P.A.: '))
c = 0

print('-=' * 25)
print('\033[;49;34mMostrando os termos da Progressão Aritmética...\033[m')

while c != 10:
  print(pa, end=' -> ')
  pa += r
  c += 1
print('Fim do programa.')
