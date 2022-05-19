#Desafio025: crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
#
n = str(input('Digite seu nome: ')).strip()
l = n.lower().split()
print('Este nome possui "Silva"? \n{}'.format('silva' in l))
