#Desafio059: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
#
soma = 0
for c in range(0,500):
  if c%2!=0:
    if c%3==0:
      print(c)
      soma += c
print(f'A soma de todos os números pares, de 1 até 500, foi de {soma}.')
print('Fim do programa.')
