#desafio37: faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles
#
x = int(input('Insira o começo da sequência: '))
y = int(input('Insira o fim da sequência:  '))

while (x<=y):
  print(x)
  x = x+1
print('Fim da contagem!')
