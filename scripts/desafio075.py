#Desafio 75: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No  final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsidere o FLAG.
#
n = s = d = 0

while n != 999:
  n = int(input('Digite um número: '))
  if n != 999:
    s += n
    d += 1
print(f'{d} números foram digitados. \nA soma entre esses números foi de {s}.')
