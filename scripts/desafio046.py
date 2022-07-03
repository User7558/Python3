#desafio0046: faça um programa que leia 5 números inteiros inseridos pelo usuário e calcule a soma destes números.
#
n = 0
s = 0

for c in range (0,5):
  n=int(input(f'Digite o {c+1}º número: '))
  s += n
print(f'\033[;35mA soma total foi {s}.\033[m')
