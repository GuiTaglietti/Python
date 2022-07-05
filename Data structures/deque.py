class Deque:
    def __init__(self):
        self.deque = []

    def addFirst(self, e):
        self.deque.insert(0, e)

    def addLast(self, e):
        self.deque.append(e)

    def lenght(self):
        return len(self.deque)

    def isEmpty(self):
        return len(self.deque) == 0

    def removeFirst(self):
        self.deque.pop(self.deque.index(self.deque[0]))

    def removeLast(self):
        self.deque.pop()

    def addArray(self, array):
        if len(self.deque) == 0:
            self.deque.extend(array)
        else:
            return "A fila já possui elementos, só é possivel adicionar array em filas vazias!"

        