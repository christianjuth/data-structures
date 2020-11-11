class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class Tree:
    def __init__(self):
        self.front = None
        
    def insert(self, data):
        node = Node(data)
        
        if self.front == None:
            self.front = node
            
        else:
            prev = None
            crnt = self.front
            
            while crnt != None:
                prev = crnt
                if data > crnt.data:
                    crnt = crnt.right
                else:
                    crnt = crnt.left
                    
            if data > prev.data:
                prev.right = node
            else:
                prev.left = node
                
    def print(self, node = None):
        crnt = node
        if crnt == None:
            crnt = self.front
        
        if crnt.left != None:
            self.print(crnt.left)
        print(crnt.data, end = "")
        print(" ", end = "")
        if crnt.right != None:
            self.print(crnt.right)
            
        if node == None:
            print("")
            
                
tree = Tree()
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(7)
tree.insert(100)

tree.print()