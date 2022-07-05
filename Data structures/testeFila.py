from fila import Fila
q = Fila()
ops = []
check = ["1", "2", "3"]

def solveAdd(var, key = 0):
    if var == "1" and key == 0:
        q.addIn(int(input("Insira o número inteiro: ")))
        ops.append("addIn() >> Adicionar um elemento (INT) à fila")
    elif var == "2" and key == 0:
        q.addIn(input("Insira a string: "))
        ops.append("addIn() >> Adicionar um elemento (STR) à fila")
    else:
        q.addIn(float(input("Insira o número de ponto flutuante (float): ")))
        ops.append("addIn() >> Adicionar um elemento (FLOAT) à fila")


print("Bem vindo ao teste de do Gui")
start = input(("Escolha:\n1 - Criar uma fila\n2 - Sair\n"))

if start == "1":
    opcoes = input("1 - Adicionar elemento por elemento\n2 - Adicionar um array\n")
    if opcoes == "1":
        while True:
            opcoes2 = input("1 - Adicionar INT\n2 - Adicionar STRING\n3 - Adicionar FLOAT\nDigite >> 0 << para parar de adicionar itens...\n")
            if opcoes2 in check:
                solveAdd(opcoes2)
                print(f"Sua fila está assim: {q.queue}")
        
            elif opcoes2 == "0":
                print(f"Sua fila ficou assim: {q.queue}")
                for i, j in enumerate(ops):
                    print(f"{i + 1}° operação: {j}")
                break

            else:
                print("Não existe essa opção!")
                while opcoes2 not in check:
                    opcoes2 = input("Insira novamente ou digite >> 0 << para sair: ")
                    if opcoes2 == "0":
                        print(f"Sua fila ficou assim: {q.queue}")
                        for i, j in enumerate(ops):
                            print(f"{i + 1}° operação: {j}")
                        break
                solveAdd(opcoes2)
                print(f"Sua fila está assim: {q.queue}")

        remove = input("Deseja remover algum item da fila?\n1 - Sim\n2- Não\n")
        if remove == "1":
            while True:
                removef = input("1 - Remover de posição específica\n2 - Remover normalmente\nDigite >> 0 << para sair\n")
                if removef == "1":
                    q.removeFrom(int(input("Indique a posição do item que deseja remover da fila:\n")))
                    print(f"Sua fila está assim: {q.queue}")
                    if q.isEmpty() == False:
                        ops.append("removeFrom() >> Remover um item de uma posição específica da fila")

                elif removef == "2":
                    q.remove()
                    print(f"Sua fila está assim: {q.queue}")
                    if q.isEmpty() == False:
                        ops.append("removeFrom() >> Remover um item de uma posição específica da fila")

                elif removef == "0":
                    print(f"Sua fila ficou assim: {q.queue}")
                    for i, j in enumerate(ops):
                        print(f"{i + 1}° operação: {j}")
                    break
        
        elif remove == "2":
            print(f"Sua fila ficou assim: {q.queue}")
            for i, j in enumerate(ops):
                print(f"{i + 1}° operação: {j}")
                        

    elif opcoes == "2":
        q.addArray(list(input("Digite o array separando cada elemento por espaço: ").split()))
        ops.append("addArray() >> Adicionar um array a fila")

        remove = input("Deseja remover algum item da fila?\n1 - Sim\n2- Não\n")
        
        if remove == "1":
            while True:
                removef = input("1 - Remover de posição específica\n2 - Remover normalmente\nDigite >> 0 << para sair\n")
                if removef == "1":
                    q.removeFrom(int(input("Indique a posição do item que deseja remover da fila:\n")))
                    print(f"Sua fila está assim: {q.queue}")
                    if q.isEmpty() == False:
                        ops.append("removeFrom() >> Remover um item de uma posição específica da fila")

                elif removef == "2":
                    q.remove()
                    print(f"Sua fila está assim: {q.queue}")
                    if q.isEmpty() == False:
                        ops.append("removeFrom() >> Remover um item de uma posição específica da fila")

                elif removef == "0":
                    print(f"Sua fila ficou assim: {q.queue}")
                    for i, j in enumerate(ops):
                        print(f"{i + 1}° operação: {j}")
                    break

elif start == "2":
    print("testeFila.py encerrado!")