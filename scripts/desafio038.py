#desafio38: faça um programa que exiba na  tela os números inteiros de 1 até 100, e a cada múltiplo de 10 (x) emita uma mensagem: "número" X "é um múltiplo de 10".
#
x = 1
while (x<=100):
  if (x%10==0):
    print('Número {} é um múltiplo de 10.'.format(x))
  else:
    print(x)
  x = x+1
print('Fim da contagem!')
