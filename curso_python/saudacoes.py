horas_str = input("Saudações, poderia me dizer que horas são? Ex. 19.30 \nR:")

try:
    horas_float = float(horas_str)
except:
    print("Você está fazendo chacota de mim...?")

if 0 <= horas_float <= 11:
    print("Obrigado, e tenha um bom dia!")
elif 12 <= horas_float <= 17:
    print("Obrigado, e tenha uma boa tarde!")
else:
    print("Oh não, estou atrasado! Obrigado, e tenha uma boa noite.")
