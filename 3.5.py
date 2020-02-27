# -----------3.5---------
from copy import deepcopy

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

class MyQueue:
    def __init__(self):
        self.stackA = Stack("A")
        self.stackB = Stack("B")
    def enqueue(self, val):
        self.stackA.push(val)
        self.remakeB()
    
    def dequeue(self):
        val = self.stackB.pop()
        self.remakeA()
        return val
        
    def remakeA(self):
        while self.stackA.top != None:
            self.stackA.pop()
        s = deepcopy(self.stackB)
        while s.top != None :
            self.stackA.push(s.pop())
    
    def remakeB(self):
        while self.stackB.top != None:
            self.stackB.pop()
        s = deepcopy(self.stackA)
        while s.top != None :
            self.stackB.push(s.pop())

myQueue = MyQueue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)

print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.stackB.show())
print(myQueue.stackA.show())
