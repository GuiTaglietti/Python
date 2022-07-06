# Gui Taglietti - OBI Solves - Prefix Sum Problem

N = int(input())
S = int(input())
lista = list(map(int, input().split()))
res = 0
quant = 0

quantPrefix = [0 for i in range(10**6)]
quantPrefix[0] = 1

for i in lista:
    quant += i
    if quant - S >= 0:
        res += quantPrefix[quant - S]
    quantPrefix[quant] += 1

print(res)
