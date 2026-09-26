import os

while True:
    os.system("clear")
    n = float(input("Digite um número: "))
    if n == int(n):
        if n % 2 == 0:
            paridade = "par"
        else:
            paridade = "impar"
    else:
        paridade = "decimal"
    if n < 0:
        positividade = "negativo"
    elif n == 0:
        positividade = "neutro"
    else:
        positividade = "positivo"
    os.system("clear")
    print(f"Seu número é {paridade} e {positividade}")
    escolha = input("Deseja escolher outro? [S/N]: ")
    if escolha == "S" or escolha == "s":
        continue
    else:
        break