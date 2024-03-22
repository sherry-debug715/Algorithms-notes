# Lintcode problem 859: https://www.lintcode.com/problem/859

import heapq
class MaxStack:
    
    def __init__(self):
        self.stack = []
        self.heap = []
        self.popped = set()
        self.count = 0
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        item = (-x, -self.count)
        self.stack.append(item)
        heapq.heappush(self.heap, item)
        self.count += 1 

    """
    @return: An integer
    """
    def pop(self):
        self.clear_removed_stack()
        item = self.stack.pop()
        self.popped.add(item)
        return -item[0]

    """
    @return: An integer
    """
    def top(self):
        self.clear_removed_stack()
        item = self.stack[-1]
        return -item[0]

    """
    @return: An integer
    """
    def peekMax(self):
        self.clear_removed_heap()
        item = self.heap[0]
        return -item[0]

    """
    @return: An integer
    """
    def popMax(self):
        self.clear_removed_heap()
        item = heapq.heappop(self.heap)
        self.popped.add(item)
        return -item[0]
    
    def clear_removed_heap(self):
        while self.heap and self.heap[0] in self.popped:
            self.popped.remove(self.heap[0])
            heapq.heappop(self.heap)

    def clear_removed_stack(self):
        while self.stack and self.stack[-1] in self.popped:
            self.popped.remove(self.stack[-1])
            self.stack.pop()

