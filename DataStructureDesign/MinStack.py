# Lintcode problem 12: https://www.lintcode.com/problem/12/

"""
Method 1:
when self.stack = [7, 6, 8, 4, 3, 4]
the relavant min_stack will be documenting the current smallest 
number, while maintaning the same length as self.stack.
self.min_stack = [7, 6, 6, 4, 3, 3]

Whenever a number is popped out of stack, a number is also popped out of min_stack
"""
class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        self.stack.append(number)
        cur_min = self.min_stack[-1] 
        if not self.min_stack or number < cur_min:
            self.min_stack.append(number)
        else:
            self.min_stack.append(cur_min)

    """
    @return: An integer
    """
    def pop(self):
        top = self.stack.pop()
        self.min_stack.pop()
        return top

    """
    @return: An integer
    """
    def min(self):
        return self.min_stack[-1]
    
"""
Method 2: A slightly optimized solution.
Instead of maintaining the same length between min_stack and stack.
Inside the min_stack, only a repeated current min val will be stored. For example:
self.stack = [1, 2, 1, 3, 1, 4]
self.min_stack = [1, 1, 1]

whenever a number is popped out of stack, compare it to the last number stored in self.min_stack, if they are the same, pop a number off min_stack as well.
"""

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        self.stack.append(number)
        if not self.min_stack:
            self.min_stack.append(number)
        else:
            cur_min = self.min_stack[-1] 
            if cur_min >= number:
                self.min_stack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        top = self.stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()
        return top

    """
    @return: An integer
    """
    def min(self):
        return self.min_stack[-1]

