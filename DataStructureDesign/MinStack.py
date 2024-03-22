# Lintcode problem 12: https://www.lintcode.com/problem/12/

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
            if cur_min < number:
                self.min_stack.append(cur_min)
            else:
                self.min_stack.append(number)

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
