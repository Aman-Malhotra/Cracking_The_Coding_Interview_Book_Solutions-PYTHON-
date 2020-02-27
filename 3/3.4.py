# --------3.4 Tower Of Hanoi Problem--------
class Node:
    def __init__(self, val, nextNode = None):
        self.val = val
        self.nextNode = nextNode
        
class Stack:
    def __init__(self, name):
        self.top = None
        self.name = name
        self.length = 0
    def push(self, val):
        n = Node(val)
        n.nextNode = self.top
        self.top = n
        self.length += 1
        return self
    
    def pop(self):
        val = self.top.val
        if(self.top !=None ):
            self.top = self.top.nextNode
            self.length -= 1
            # print("The length of the stack after pop is ", self.length)
        else:
            self.top = None
        return val
    
    def show(self):
        temp = self.top
        while(temp):
            print("Value in stack ", self.name, " : ",temp.val)
            temp = temp.nextNode

def toh(n, fromStack, toStack, auxStack):
    if(n == 1):
        toStack.push(fromStack.pop())
        print("Move ", n)
        return 
    toh(n-1, fromStack, auxStack, toStack)
    print("Move ", n)
    toStack.push(fromStack.pop())
    toh(n-1, auxStack, toStack, fromStack)
    
stackA = Stack("A")
stackB = Stack("B")
stackC = Stack("C")
n = int(input())
for i in range(n,0, -1 ):
    stackA.push(i)
toh(n, stackA, stackC, stackB)
stackA.show()
stackB.show()
stackC.show()
