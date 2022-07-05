class Node:
    def __init__(self, element):
        self.element = element
        self.rightNode = None
        self.leftNode = None
        
class Tree:
    def __init__(self, element = None):
        if element:
            self.root = Node(element)
        else:
            self.root = None

    def orderedTraversal(self, node = None):
        if node is None:
            node = self.root
        if node.leftNode:
            self.orderedTraversal(node.leftNode)
        if node.rightNode:
            self.orderedTraversal(node.rightNode)

    def height(self, node = None):
        lh = 0
        rh = 0
        if node is None:
            node = self.root
        if node.leftNode:
            lh = self.height(node.leftNode)
        if node.rightNode:
            rh = self.height(node.rightNode)
        if lh > rh:
            return lh + 1
        else:
            return rh + 1        