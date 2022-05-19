'''desafio026: faça um programa que leia uma frase pelo teclado e mostre:
quantas vezes aparece a letra 'a'
em que posição ela aprece pela primeira vez
em que posição ela aparece pela ultima vez'''
#
f = str(input('Digite uma frase: ')).strip().upper()
print('''ANALISANDO FRASE
=================
Quantas vezes você digitou a letra "a" na frase: {}
Qual a posição da primeira letra "a" na frase: {}
Qual a posição da ultima letra "a" na frase: {}'''.format(f.count('A'), f.find('A')+1, f.rfind('A')+1))
