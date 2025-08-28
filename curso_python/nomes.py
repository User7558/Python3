nome = input("Fale-me seu nome, e julgarei-te por isso! \nR:")

tamanho = len(nome)

if tamanho <= 4:
    print("Um nome simples, curto... Uma pessoa de poucas palavras, presumo.")
elif 5 <= tamanho <= 6:
    print("Um nome normal, para uma pessoa normal... Satisfatório.")
else:
    print("Quem é você, um nobre? Desnecessariamente grande!")
