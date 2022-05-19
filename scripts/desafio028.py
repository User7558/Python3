#desafo28: escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário perdeu ou venceu.
#
from random import randint
from time import sleep
print('JOGO DA ADVINHAÇÃO V1.0')
print('-' * 30)
j = int(input('Digite um número de 0 a 5: '))
pc = randint(0,5)
print('Processando...')
sleep(2) #faz com que o computador espere determinado tempo antes de exibir a proxima mensagem
print('Número escolhido pelo computador: {}!'.format(pc))
if (pc == j):
    print('Parabéns, você venceu o jogo da adivinhação!')
else:
    print('Que pena, você perdeu o jogo da adivinhação! Tente novamente :)')
