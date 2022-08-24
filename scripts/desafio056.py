#Desafio056: Crie um programa que faça o programa jogar Jokenpô com você.
#
from random import choice
from time import sleep

print('='*15)
print('JO-KEN-PÔ!')
print('='*15)
print('Desafie a máquina em um jogo de Jokenpô!')
p = str(input('''Qual será sua escolha?
- Pedra
- Papel
- Tesoura
---------------
R: ''')).lower()
x = choice(['pedra','papel','tesoura'])

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
sleep(0.2)

if p==x:
    print(f'O usuário e a máquina pensaram igual, ambos jogaram {x}! \nO resultado foi: EMPATE.')
elif p!=x:
    if p=='pedra' and x=='papel':
        print(f'Jogada do usuário: {p} \nJogada da máquina: {x} \nO resultado foi: A MÁQUINA GANHOU.')
    elif p=='pedra' and x=='tesoura':
        print(f'Jogada do usuário: {p} \nJogada da máquina: {x} \nO resultado foi: O USUÁRIO GANHOU.')
    elif p=='papel' and x=='pedra':
        print(f'Jogada do usuário: {p} \nJogada da máquina: {x} \nO resultado foi: O USUÁRIO GANHOU.')
    elif p=='papel' and x=='tesoura':
        print(f'Jogada do usuário: {p} \nJogada da máquina: {x} \nO resultado foi: A MÁQUINA GANHOU.')
    elif p=='tesoura' and x=='pedra':
        print(f'Jogada do usuário: {p} \nJogada da máquina: {x} \nO resultado foi: A MÁQUINA GANHOU.')
    elif p=='tesoura' and x=='papel':
        print(f'Jogada do usuário: {p} \nJogada da máquina: {x} \nO resultado foi: O USUÁRIO GANHOU.')

sleep(1)
print('Foi bom jogar com você, até!')