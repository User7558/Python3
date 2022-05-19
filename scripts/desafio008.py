#desafio08: um programa que leia o valor em métros e exiba convertido em centímeotrs e milímetros
#
m=float(input('Digite o valor em metros: '))
cm = m*100
mm = m*1000
print('Metros: {} \nCentímetros: {} \nMilímetros: {}'.format(m, cm, mm))
