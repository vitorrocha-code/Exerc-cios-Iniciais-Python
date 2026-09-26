import os
numeros = []
while True:
    os.system("clear")
    n = float(input("Digite o número: "))
    numeros.append(n)
    escolha = input("Deseja digitar outro número? [S/N]: ")
    if escolha == "S" or escolha == "s":
        continue
    else:
        break

menor = numeros[0]
maior = numeros [0]

for n in numeros:
    if n > maior:
        maior = n

for n in numeros:
    if n < menor:
        menor = n

print(f"O menor número é {menor} e o maior é {maior}")