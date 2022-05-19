#desafio19: um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude-o, lendo os nomes e escrevendo o escolhido.
#
import random
n1=input('Nome 1: ')
n2=input('Nome 2: ')
n3=input('Nome 3: ')
n4=input('Nome 4: ')
lista = [n1, n2, n3, n4]
print('O nome escolhido foi {}'.format(random.choice(lista)))
