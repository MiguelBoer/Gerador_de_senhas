import secrets
import string

while True:
    while True:
        try:
            tamanho = int(input("Qual o tamanho da senha que voce desejas?\n"))
            break
        except ValueError:
            print("Digite apenas números!")

    while True:
        especial = input("Deseja colocar caracteres especiais?\n [sim]/[não]\n").strip().lower()
        if especial == "sim" or especial == "não" or especial == "nao":
            break
        print("Digite apenas 'sim' ou 'não'!")

    while True:
        n = input("Deseja adicionar numeros?\n [sim]/[não]\n").strip().lower()
        if n == "sim" or n == "não" or n == "nao":
            break
        print("Digite apenas 'sim' ou 'não'!")

    alfabeto = string.ascii_letters

    if especial == "sim":
        alfabeto = alfabeto + string.punctuation

    if n == "sim":
        alfabeto = alfabeto + string.digits

    senha = ""
    for i in range(tamanho):
        senha += secrets.choice(alfabeto)

    print("Sua senha é:", senha)

    while True:
        continuar = input("Deseja criar outra senha?\n [sim]/[não]\n").strip().lower()
        if continuar == "sim" or continuar == "não" or continuar == "nao":
            break
        print("Digite apenas 'sim' ou 'não'!")

    if continuar == "não":
        print("Obrigado por testar meu codigo :)")
        break