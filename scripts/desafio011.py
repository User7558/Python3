#desafio11: um programa que leia a altura e largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
#
a=float(input('Digite, em metros, a altura da parede: '))
l=float(input('Digite, em metros, a largura da parede: '))
a = a*l
t = a/2
print('A quantidade de tinta necessária para pintar uma parede de área {:.2f} será de {}L.'.format(a, t))