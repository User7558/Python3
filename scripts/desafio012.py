#desafio12: algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
#
po=float(input('Qual o preço deste produto? R$'))
pn = po-(po*(5/100))
print('O preço deste mesmo produto com 5% de desconto é de R${:.2f}'.format(pn))