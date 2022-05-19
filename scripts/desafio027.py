#desafio027: faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o segundo nome separadamente
#
n = str(input('Digite seu nome completo: ')).strip()
ln = n.split()
print('''Olá, prazer em conhecê-lo! Vamos analisar seu nome...
Seu primeiro nome é {}
Seu último nome é {}'''.format(ln[0], ln[len(ln)-1]))
