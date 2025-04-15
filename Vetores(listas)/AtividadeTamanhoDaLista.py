itens = []
print("Bem vindo a lista de itens automática")
while True:
    print('')
    print("1 para adicionar um item na lista")
    print("2 para remover um item da lista")
    print("3 para ver o tamnho da lista")
    print("4 para ver os itens da lista")
    print("5 para sair")
    print(" ")
    desisao = int(input("O que deseja fazer?: "))
    if desisao == 1:
     itens.append(input("Adicione o item: "))
     continue
    elif desisao == 2:
        itens.remove(input("Qual item deseja remover: "))
        continue
    elif desisao == 3:
        tamanhodalista =len(itens)
        print(f"O tamanho da lista é: {tamanhodalista}")
    elif desisao == 4:
        print("Os itens da lista são:")
        for i in itens:
            print(i)

    elif desisao == 5:
        print("Obrigado por usar a lista automática!")
        break
    else:
        print("Esse comando não existe!")





