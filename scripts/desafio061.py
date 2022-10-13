#Desafio061: Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
#
s = 0
cont = 0
for c in range (0,6):
  n = int(input(f'Digite o {c+1}º número: '))
  if n%2==0 and n!=0:
    s += n
    cont += 1
print(f'Foram digitados {cont} números pares.')
print(f"A soma dos números pares digitados foi de {s}.")
