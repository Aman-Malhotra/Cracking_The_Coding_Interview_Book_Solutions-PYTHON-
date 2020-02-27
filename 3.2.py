# --------3.2 Stack min value in o(1) time--------
class Node:
    def __init__(self, val, nextNode = None):
        self.val = val
        self.nextNode = nextNode
        self.minValue = None

class Stack:
    def __init__(self):
        self.top = None
        self.minValue = None
    def push(self, val):
        n = Node(val)
        n.nextNode = self.top
        
        if(self.top != None and self.top.minValue != None):
            n.minValue = min(self.top.minValue , n.val)
        else:
            n.minValue = val
        self.top = n
    
    def pop(self):
        self.top = self.top.nextNode
    
    def show(self):
        temp = self.top
        while(temp):
            print(temp.val)
            temp = temp.nextNode
            
    def printMin(self):
        print(self.top.minValue)

s = Stack()
s.push(3)
s.push(4)
s.push(1)
s.push(6)
s.push(5)
s.push(2)
s.show()
s.printMin()
