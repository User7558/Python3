'''Desafio053: Refaça o exercício 35 dos triêngulos, acrescentando o recusro de mostrar que tipo de triângulo será formado:
Equilátero - todos os lados iguais
Isósceles - dois lados iguais
Escaleno - todos os lados diferentes'''
#
base = float(input('Informe o tamanho do primeiro lado: '))
lado1 = float(input('Informe o tamanho do segundo lado: '))
lado2 = float(input('Informe o tamanho do terceiro lado: '))

if base < lado1 + lado2 and lado1 < base + lado2 and lado2 < base + lado1:
  print('O triângulo É possivel neste caso.')
  if base==lado1==lado2:
    print('O triângulo será equilátero.')
  elif base==lado1 or base==lado2 or lado1==lado2:
    print('O triângulo será isósceles.')
  else:
    print('O triângulo será escaleno.')
else:
  print('O triângulo NÃO é possível neste caso.')
