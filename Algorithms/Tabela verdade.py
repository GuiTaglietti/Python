import ttg as t
from time import sleep

operadores = ["not", "~", "and", "or", "=", "=>", "(", ")"]
operandos = []

print("Tutorial do programa!\nUse os seguintes operadores EM INGLES!: nao = not , ~  /  e = and / ou = or /\ncondicional = => / bicondicional = = (Sinal de igual) / Disj. Exclusiva = xor")
print("Exemplos de expressões: p and q and r / p or q or r / (p or (~q)) => r")

sleep(3)

print("O programa trabalha com até 6 PROPOSIÇÕES (p, q, r ...)")
props = int(input("Digite quantas proposições existem na expressão (de 1 a 6): "))

if props == 1:
    tabela = t.Truths([input("Insira a 1 proposição: ")], [input("Insira a expressão: ")])
    print(tabela)

elif props == 2:
    tabela = t.Truths([input("Insira a 1 proposição: "), input("Insira a 2 proposição: ")], [input("Insira a expressão: ")])
    print(tabela)

elif props == 3:

    tabela = t.Truths([input("Insira a 1 proposição: "), input("Insira a 2 proposição: "), input("Insira a 3 proposição: ")], [input("Insira a expressão: ")])
    print(tabela)

elif props == 4:
    tabela = t.Truths(
        [input("Insira a 1 proposição: "), input("Insira a 2 proposição: "), input("Insira a 3 proposição: "),
         input("Insira a 4 proposição: ")], [input("Insira a expressão: ")])
    print(tabela)

elif props == 5:
        tabela = t.Truths(
        [input("Insira a 1 proposição: "), input("Insira a 2 proposição: "), input("Insira a 3 proposição: "),
         input("Insira a 4 proposição: "), input("Insira a 5 proposição: ")], [input("Insira a expressão: ")])
        print(tabela)

else:
    tabela = t.Truths(
        [input("Insira a 1 proposição: "), input("Insira a 2 proposição: "), input("Insira a 3 proposição: "),
         input("Insira a 4 proposição: "), input("Insira a 5 proposição: "), input("Insira a 6 proposição: ")],
        [input("Insira a expressão: ")])

    print(tabela)

