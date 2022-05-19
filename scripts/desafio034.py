#desafio34: escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salário superiores a R$1.250,00 calcule aumento de 10%, para os inferiores ou iguais, aumento de 15%.
#
s = int(input('Insira o salário do funcionário: R$'))
if (s<=1250):
    sa = s+(s*(15/100))
    print('O aumento salarial deixará o salário em R${:.2f}'.format(sa))
else:
    sa = s+(s*(10/100))
    print('O aumento salarial deixará o salário em R${:.2f}'.format(sa))
