# Gui Taglietti - OBI Solves

start = int(input())
end = int(input())
soma = int(input())

while True:
    array = []
    end = str(end)
    for i in end:
        array.append(i)
    maxnum = "+".join(array)
    maxnum = eval(maxnum)
    if maxnum == soma:
        print(end)
        break
    else:
        end = int(end) - 1
        if end == start:
            print(-1)
            break 
