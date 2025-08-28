num_str = input("Digite um número inteiro, e derramarei minha sabedoria sobre você, mero mortal! \nR:")

try:
    num_int = int(num_str)
except:
    print("Não tente me enganar, digite algo que posso usar!")

par_ou_impar = (num_int % 2 == 0)

if par_ou_impar:
    print("Com meu infinito conhecimento, consigo dizer que o número digitado é PAR!")
else:
    print("Com meu infinito conhecimento, consigo dizer que o número digitado é IMPAR!")
