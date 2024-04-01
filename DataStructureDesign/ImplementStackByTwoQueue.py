# Lintcode problem 494: https://www.lintcode.com/problem/494/?fromId=161&_from=collection

"""
The logic is to always keep the newly pushed number at the begining of a queue. Therefore, we need to make sure queue2 is always empty, using it to add a new number, then move all numbers from queue1 to queue2 in FIFO order. 
Last, swap queue1 and queue2 to keep queue2 empty again.
"""
from collections import deque

class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.queue1 = deque([])
        self.queue2 = deque([])

    def push(self, x): # O(N) where N is the length of queue1
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
    """
    @return: nothing
    """
    def pop(self): # O(1)
        self.queue1.popleft()

    """
    @return: An integer
    """
    def top(self): # O(1)
        return self.queue1[0]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self): # O(1)
        return not self.queue1
