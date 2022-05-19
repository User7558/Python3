'''desafio022: crie um programa que leia o nome completo de uma pessoa e mostre:
o nome com todas as letras maiusculas
o nome com todas as letras minusculas
quantas letras ao todo (sem considerar os espaços)
quantas letras tem o primeiro nome'''
#
name = str(input('Qual seu nome completo: ')).strip()
nl = name.split()
print('''EXIBINDO INFORMAÇÕES:
=====================
Todas as letras em maiúsculas: {}
Todas as letras em minúsculas: {}
Quantas letras tem seu nome: {}
Quantas letras tem seu primeiro nome: {}'''.format(name.upper(), name.lower(), len(name.replace(" ", "")), len(nl[0])))
