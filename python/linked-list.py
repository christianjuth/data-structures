class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        
        
class LinkedList:
    def __init__(self):
        self.front = None
        self.last = None
        
    def push(self, data):
        node = Node(data)
        
        if self.front == None:
            self.front = node
            self.last = node
            
        else:
            self.last.next = node
            self.last = node
        
    def print(self):
        i = 0
        crnt = self.front
        while crnt != None:
            # print separator
            if i > 0:
                print(", ", end = "")
            # print data    
            print(crnt.data, end = "")
            crnt = crnt.next
            i += 1
        
        print("")
        
    def remove(self, data):
        prev = None
        crnt = self.front
        while crnt != None:
            # print separator
            if crnt.data == data:
                # first item in list
                if prev == None:
                    self.front = crnt.next
                # not first item in list
                else:
                    prev.next = crnt.next
                crnt = crnt.next
                    
            else:
                prev = crnt
                crnt = crnt.next
                
            
                
        
list = LinkedList()
list.push(4)
list.push(5)
list.push(3)
list.print()
list.remove(5)
list.print()