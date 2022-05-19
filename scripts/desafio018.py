#desafio18: um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste ângulo
#
import math

a=float(input('Insira o valor do ângulo: '))
c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
tg = math.tan(math.radians(a))
print('Ângulo: {} \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(a, s, c, tg))
