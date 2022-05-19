#desafio35: desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#
a = float(input('Informe a primeira reta: '))
b = float(input('Informe a segunda reta: '))
c = float(input('Informe a terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('O triângulo É possivel neste caso.')
else:
    print('O triângulo NÃO é possível neste caso.')
