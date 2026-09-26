import os 

def menu_principal():
    os.system("clear")
    print("-------------------")
    print("Escolha uma opção:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    opcao = input("Escolha:")
    return opcao 



def numeros():
    os.system('clear')
    n1 = float(input("Digite o primeiro numero:"))
    n2 = float(input("Digite o segundo numero:"))
    return [n1, n2]

def soma():
    soma = numero[0] + numero[1]
    print(f"O resultado é {soma}")

def subtracao():
    sub = numero[0] - numero[1]
    print(f"O resultado é {sub}")

def multiplicacao():
    mult = numero [0]*numero[1]
    print(f"O resultado é {mult}")

def divisao():
    div = numero[0]/numero[1]
    print(f"O resultado é {div}")

while True:
    opcao = menu_principal()
    numero = numeros()
    if opcao == "1":
        soma()
        input("")
    elif opcao =="2":
        subtracao()
        input("")
    elif opcao == "3":
        multiplicacao()
        input("")

    elif opcao == "4":
        divisao()
        input("")
    else:
        print("opcao invalida")
        input("")

    os.system("clear")
    escolha = input("Deseja fazer outra conta? [S/N]: ")
    if escolha == "S" or escolha == "s":
        continue
    else:
        break