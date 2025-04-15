lista = []
def listarnome():
    for index, nome in enumerate(lista):
        print(index + 1, nome)


def inserirnome(nomepet):
    if nomepet != "":
     lista.append(nomepet)
     print(f"O pet {nomepet} foi inserido com sucesso!")
     listarnome()

    else:
     print("Insira um nome válido.")



def removernome(nomepet):
    if nomepet in lista:
        lista.remove(nomepet)
        print(f"O pet {nomepet} foi removido com sucesso!")
        listarnome()
    else:
        print("Digite um nome válido.")

while True:
    print("Escreva uma das opções: Adicionar nome / Remover nome / Listar nome")
    ops = input("Escolha uma das opções: ")

    if ops == "Adicionar nome":
        nomepet = input("Digite o nome do PET: ")
        inserirnome(nomepet)

    elif ops == "Listar nome":
        listarnome()
    else:
        print("Comando inválido ")
        break








