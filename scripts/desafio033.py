# desafio33: faça um programa que leia três números e mostre qual é o maior e qual o menor
#
from time import sleep

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# verificando o menor
me = a
if b < a and b < c:
    me = b
else:
    if c < a and c < b:
        me = c
# verificando o maior
ma = a
if b > c and b > a:
    ma = b
else:
    if c > b and c > a:
        ma = c
print('Menor valor digitado: {} \nMaior valor digitado: {}'.format(me, ma))
