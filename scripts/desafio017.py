#desafio17: um programa que leia o valor do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
#
from math import hypot

ca=float(input('Digite o valor do cateto adjacente: '))
co=float(input('Digite o valor do cateto oposto: '))
print('A hipotenusa deste triângulo é {:.2f}.'.format(hypot(co,ca)))