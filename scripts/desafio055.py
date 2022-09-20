'''Desafio055: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
- à vista dinehiro/cheque: 10% de desconto;
- à vista no cartão: 5% de desconto;
- em até 2x no cartão: preço normal;
- 3x ou mais vezes no cartão: 20% de juros.'''
#
x = float(input('Qual o preço do produto que deseja comprar? R$'))
fp = int(input('''Qual a forma de pagamento?
[1] Dinheiro
[2] Cartão
[3] Cheque
------------------------------------------------
R: '''))

if fp==1:
    d = (x*10)/100
    x = x-d
    print(f'O desconto oferecido graças a forma de pagamento de seu produto foi de 10%, o valor passará a ser R${x:.2f}.')
elif fp==2:
    p = int(input('''Em quantas parcelas pagará seu produto?
---------------
R: '''))
    if p==1:
        d = (x*5)/100
        x = x-d
        print(f'O desconto oferecido graças a forma de pagamento de seu produto foi de 5%, o valor passará a ser R${x:.2f}.')
    elif p==2:
        parc= x/p
        print(f'A forma de pagamento escolhida não dá direito a desconto, o valor a ser pago será de R${x:.2f}, parcelado em {p} vezes de R${parc:.2f}.')
    elif p>=3:
        d = (x*20)/100
        x += d
        parc=x/p
        print(f'O juros agregado graças a forma de pagamento de seu produto foi de 20%, o valor passará a ser R${x:.2f}, parcelado em {p} vezes de R%{parc:.2f}.')
else:
    d = (x*10)/100
    x = x-d
    print(f'O desconto oferecido graças a forma de pagamento de seu produto foi de 10%, o valor passará a ser R${x:.2f}.')