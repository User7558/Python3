#desafio13: algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
#
s=float(input('Qual seu salário atual? R$'))
sa = s+(s*(15/100))
print('Parabens, você recebeu um aumento salarial! \nSeu novo salário é de R${:.2f}!'.format(sa))