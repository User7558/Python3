#Desafio023: faça um programa que leia um núero de 0 a 9999 e mostre na tela cada um dos digitos separados
#
n=int(input('Digite um núero de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('''Número Digitado: {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(n, u, d, c, m))
