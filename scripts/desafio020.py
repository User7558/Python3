#desafio20: o mesmo professor do desafio anterior quer sortear a ordem da apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#
from random import shuffle
n1=input('Nome 1: ')
n2=input('Nome 2: ')
n3=input('Nome 3: ')
n4=input('Nome 4: ')
lista = [n1, n2, n3, n4]
print('Ordem escolhida: \n', shuffle(lista))
