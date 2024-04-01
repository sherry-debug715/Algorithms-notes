# Lintcode problem 40: https://www.lintcode.com/problem/40/?fromId=161&_from=collection

class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element): # O(1)
        self.stack1.append(element)

    """
    @return: An integer
    """
    def pop(self): # Worst case: O(N), on average: O(1)
        if not self.stack2:
            self.pop_stack() 
        val = self.stack2.pop()
        return val

    """
    @return: An integer
    """
    def top(self): # Worst case: O(N), on average: O(1)
        if not self.stack2:
            self.pop_stack()
        return self.stack2[-1]

    def pop_stack(self): # O(N)
        while self.stack1:
            cur = self.stack1.pop()
            self.stack2.append(cur) 
        
