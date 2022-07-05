class Pilha:
    def __init__(self):
        self.array = []

    def addStack(self, element):
        self.array.append(element)

    def addArray(self, array):
        self.array.extend(array)

    def removeStack(self):
        self.array.pop()

    def lenght(self):
        return len(self.array)

    def isEmpty(self):
        return len(self.array) == 0

        