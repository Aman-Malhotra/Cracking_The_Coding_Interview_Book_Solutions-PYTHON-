# --------3.3 SetOfStacks--------
class Node:
    def __init__(self, val, nextNode = None):
        self.val = val
        self.nextNode = nextNode
        
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    def push(self, val):
        n = Node(val)
        n.nextNode = self.top
        self.top = n
        self.length += 1
        return self
    
    def pop(self):
        if(self.top !=None ):
            self.top = self.top.nextNode
            self.length -= 1
            # print("The length of the stack after pop is ", self.length)
        else:
            self.top = None
        
        return self
    
    def show(self):
        temp = self.top
        while(temp):
            print(temp.val)
            temp = temp.nextNode

class SetOfStacks:
    def __init__(self):
        self.current = None
        self.stacks = []
        
    def push(self, val):
        if(len(self.stacks)==0):
            s = Stack()
            s.push(val)
            self.stacks.append(s)
            self.current = 0
        elif(self.current != None and self.current < len(self.stacks)):
            # print(" Else if Working for ", val)
            # print("This is the value for current ", self.current)
            if(self.stacks[self.current].length == 2):
                s1 = Stack()
                s1.push(val)
                self.stacks.append(s1)
                # print("New Stack number ", len(self.stacks))
                self.current += 1
            else:
                self.stacks[self.current].push(val)
                
    def pop(self):
        if(self.stacks[self.current].length>0):
            self.stacks[self.current].pop()
        elif self.current > 0 :
            self.current -= 1
            self.stacks[self.current].pop()
    
    def popAt(self, index):
        if(self.stacks[self.current].length>0):
            self.stacks[self.current].pop()
        elif self.current > 0 :
            self.current -= 1
            self.stacks[self.current].pop()
            
    def printAll(self):
        for s in self.stacks:
            s.show()

s = SetOfStacks()

s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
s.pop()
s.pop()
s.pop()
s.pop()

s.printAll()
