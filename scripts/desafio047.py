'''desafio047: faça um programa que leia um número entre 1 e 7 e exiba a mensagem do dia da semana correspondente e todos os seus sucessores até o Sábado.
Exemplo, caso a pessoa digite 4 será exibido:
Quarta-Feira
Quinta-Feira
Sexta-Feira
Sábado.'''
#
from time import sleep

semana = ['','Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']
n = int(input('Digite um número entre 1 e 7: '))

print('\033[;033mEXIBINDO SEMANA...\033[m')
sleep(1)

while n <= 7:
  print(semana[n])
  n += 1
