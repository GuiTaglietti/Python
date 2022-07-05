def greedy(value, array = [1, 2, 5, 10, 20, 50, 100, 1000]):
    arrayFinal = []
    controller = len(array) - 1
    while True:
        if value >= array[controller]:
            value -= array[controller]
            arrayFinal.append(array[controller])
        elif value == 0:
            return arrayFinal
            break
        else:
            controller -= 1
        
var = int(input("Digite o valor que deseja usar: "))

for i in range(len(greedy(var))):
    print(greedy(var)[i])
