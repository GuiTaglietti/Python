# Gui Taglietti - OBI Solves

countRows = 0
matriz = []
for i in range(int(input())):
    matriz.append(list(map(int, input().split())))

for i in range(len(matriz)):
    try:
        countCols = matriz[i].index(0)
        if countCols:
            break
    except ValueError:
        countRows += 1
        continue

while True:
    testCase = -1
    try:
        somaf = sum(matriz[countRows + testCase])
        if somaf != 0: break
    except:
        testCase = 1

final = somaf - sum(matriz[countRows])

print(f"{final}\n{countRows + 1}\n{countCols + 1}")
