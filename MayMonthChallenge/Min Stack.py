"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.






"""
class MinStack:

    def __init__(self):
        self.lst : list = []
        self.temp: list = []
        

    def push(self, x: int) -> None:
        self.lst.append(x)
        if(len(self.lst) > 0):
            if(len(self.temp)>0):
                if(x <= self.temp[len(self.temp)-1]):
                    self.temp.append(x)
            else:
                self.temp.append(x)
       
        

    def pop(self) -> None:
        if(len(self.lst) > 0 ):
            x = self.lst.pop()
            if(x == self.temp[len(self.temp)-1]):
                self.temp.pop()
        else:
            if(len(self.temp) > 0):
                self.temp.pop()
        
        

    def top(self) -> int:
        if(len(self.lst) != 0):
            return self.lst[len(self.lst)-1]
       

    def getMin(self) -> int:
        if(len(self.temp) > 0):
            return self.temp[len(self.temp)-1]