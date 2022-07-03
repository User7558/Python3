#desafio044: Faça um programa que determine o maior dentre varios números inteiros positivos. A condição para fechar o programa é o usuário digitar o número 0.
#
n = -1
mn = 0

while n!=0:
  n = int(input('\033[0;32m[PARA SAIR DIGITE 0]\033[m1 \nBoas vindas, digite um número:'))
  if n>mn:
    mn = n
print(f'O maior número digitado foi {mn}.')