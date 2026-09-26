import os
usuarios= []

def menu():
    os.system("clear")
    print("===============================")
    print("---------SEJA BEM-VINDO--------")
    print("===============================")
    print("ESCOLHA UMA OPÇÃO:")
    print("1 - CADASTRAR USUÁRIO")
    print("2 - LISTAR USUÁRIO")
    print("3 - REMOVER USUÁRIO")
    print("4 - SAIR")
    escolha = input("DIGITE A OPÇÃO DESEJADA: ")
    return escolha


def cadastro():
    os.system("clear")
    print("===============================")
    print("------------CADASTRO-----------")
    print("===============================")
    nome = input("Digite seu nome (login): ")
    email = input("Digite seu email: ")
    senha = input ("Digite sua senha: ")
    if nome ==  "" or email == "" or senha == "":
        print("Algum dos campos não foi preenchido corretamente, falha no cadastro")
        input("APERTE ENTER PARA CONTINUAR")
    else:
        novo_usuario = {"nome":nome, "email": email,"senha":senha}
        print("Cadastro concluido com suceso")
        input("APERTE ENTER PARA CONTINUAR")
        return novo_usuario


def lista():
    os.system("clear")
    contador = 0
    for usuario in usuarios:
        contador +=1
        print(f"{contador} - Nome: {usuario["nome"]}, email: {usuario["email"]}, senha: {usuario["senha"]}")
        input("PRECIONE O ENTER PARA CONTINUAR")


def remover():
    os.system("clear")
    lista()
    opcao = int(input("DIGITE O NÚMERO DO USUARIO QUE VOCÊ DESEJA EXCLUIR: "))
    opcao -= 1
    if opcao == int(opcao) and opcao > -1 and opcao <= len(usuarios):
        del usuarios[opcao]
        print("USUARIO DELETADO")
        input("PRECIONE O ENTER PARA CONTINUAR")
    else:
        print("Digite uma opção válida")
        input("PRECIONE O ENTER PARA CONTINUAR")


while True:
    escolha = menu()
    if escolha == "1":
        novo_usuario = cadastro()
        usuarios.append(novo_usuario)
    elif escolha == "2":
        lista()
    elif escolha == "3":
        remover()
    elif escolha == "4":
        break
    else:
        print("Digite uma opção valida")