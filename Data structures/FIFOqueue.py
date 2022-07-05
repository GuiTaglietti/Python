class Fila:
    def __init__(self):
        self.queue = []

    def addIn(self, item):
        self.queue.append(item)

    def remove(self):
        try:
            self.queue.pop(self.queue.index(self.queue[0]))
        except IndexError:
            return "Não existe elemento a ser removido na posição indicada!"

    def removeFrom(self, pos):
        try:
            self.queue.pop(self.queue.index(self.queue[pos]))
        except IndexError:
            return "Não existe elemento a ser removido na posição indicada!"

    def isEmpty(self):
        return len(self.queue) == 0

    def clear(self):
        self.queue = []
    
    def addArray(self, array):
        self.queue.extend(array)

    def queueLenght(self):
        return len(self.queue)
    
   
