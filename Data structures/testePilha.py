from pilha import Pilha
p = Pilha()
ops = []

print("Bem vindo ao teste do Gui")
print("Escolha uma das opções:\n1 - Criar uma pilha \n2 - Comandos")
teste = input()

if teste == "1":
    op = input("Escolha:\n1 - Adicionar elemento por elemento\n2 - Adicionar uma lista (array, vetor) inteiro(a)\n")
    if op == "2":
        lista = p.addArray(list(input("Digite varios itens separados por espaço: ").split()))
        if p.isEmpty() == False:
            print("Array adicionado com sucesso na pilha")
            ops.append("addArray() = Adicionou um array inteiro")
        else:
            print("Erro ao adicionar array")

    elif op == "1":
        item = input("Digite o item que deseja adicionar: ")
        p.addStack(item)
        ops.append("addStack() = Adicionar um item na lista")
        continuar = input("Deseja adicionar mais itens?\n1 = Sim\n2 = Não\n").lower()
        if continuar == "sim" or continuar == "1":
            while True:
                item = input("Digite o item que deseja adicionar | Digite 0 para parar: ")
                if item == "0":
                    break
                else:
                    p.addStack(item)
                    ops.append("addStack() = Adicionar um item na lista")
        elif continuar == "nao" or continuar == "não" or continuar == "2":
            pass
        else:
            print("Não existe essa opção!")
    else:
        print("Não existe essa opção!")

elif teste == "2":
    print("Comandos abaixo para mexer na classe e editar o programa:")
    print("addStack() = Adiciona um item único na pilha\naddArray() = Adiciona um array inteiro na pilha")
    print("removeStack() = Remove o ultimo item adicionado na pilha\nlenght() = Retorna o tamanho da pilha")
    print("isEmpty() = Retorna um valor booleano em relação a pilha estar vazia ou não")

if teste == "1":
    print(f"Sua pilha: {p.array}\nTamanho da pilha: {p.lenght()}\nOperações realizadas: ")
    for i in ops:
        print(i)
    ops = []
    remover = input("Deseja remover algum item da pilha?\n1 - Sim\n2 - Não\n")
    if remover == "1":
        try:
            p.removeStack()
        except IndexError:
            print(f"Não existe itens para remover!\nSua pilha: {p.array}")
        
        ops.append("removeStack() = Remover item da pilha")
        print(f"Sua pilha está assim: {p.array}")
        continuar = input("Deseja continuar removendo?\n1 - Sim\n2 - Não\n")
        if continuar == "1":
            while True:
                parar = input("\nPara parar de remover digite 0 | Para continuar digite 1:\n")
                if parar == "1":
                    try:
                        p.removeStack()
                    except IndexError:
                        print(f"Não existe mais itens para remover!\nSua pilha: {p.array}")
                    
                    ops.append("removeStack() = Remover item da pilha")
                    print(f"Sua pilha está assim: {p.array}")
                else:
                    print(f"Sua pilha: {p.array}\nTamanho da pilha: {p.lenght()}\nOperações realizadas: ")
                    for i in ops:
                        print(i)
                    ops = []
                    break