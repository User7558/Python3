#desafio29: escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa custará R$7.00 por cada km acima do limite
#
km = int(input('Informe a velocidade de seu carro: '))
if (km > 80):
    m = 7*(km-80)
    print('Você foi multado! Valor da multa: R${:.2f}'.format(m))
else:
    print('Você está dirigindo seguindo as leis e não recebeu nenhuma multa, parabéns!')
