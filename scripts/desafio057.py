#Desafio057: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
#
from time import sleep

for c in range (10, 0, -1):
  print(c)
  sleep(1)
print('\033[5;49;32mF\033[5;49;34mE\033[5;49;35mL\033[5;49;33mI\033[5;49;34mZ\033[5;49;31m A\033[5;49;35mN\033[5;49;33mO\033[5;49;36m N\033[5;49;32mO\033[1;49;31mV\033[0;49;34mO\033[5;49;39m!\033[m')
