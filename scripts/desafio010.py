#desafio10: programa que le quanto dinheiro uma pessoa tem em sua carteira e quantos dólares ela pode comprar. Considerando US$1=R$3.27
#
rs=float(input('Dinheiro real: R$'))
d = rs/3.27
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(rs, d))