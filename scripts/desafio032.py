#desafio32: faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#
from datetime import date
a = int(input('Qual ano será analisado? Pressione 0 para analisar o ano atual '))
if (a==0):
    a = date.today().year #pega o ano atual configurado na máquina
if (a%4==0 and a%100!=0 or a%400==0):
    print('O ano {} é um ano bissexto!'.format(a))
else:
    print('O ano {} não é um ano bissexto.'.format(a))
