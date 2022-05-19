#desafio024: crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
#
n = str(input('Digite o nome da cidade: ')).strip()
print('A cidade {} começa com o nome "Santo"? \n{}'.format(n, 'Santo' in n.capitalize()))
