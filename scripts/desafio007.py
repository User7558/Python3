#desafio07: programa que leia duas notas de um aluno, calcule-as e mostre sua média
#
nome=input('Nome do aluno: ')
n1=int(input('Primeira nota: '))
n2=int(input('Segunda nota: '))
m = (n1+n2)/2
print('A média de {} foi de {:.1f}.'.format(nome, m))