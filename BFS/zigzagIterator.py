# Lintcode problem 541: https://www.lintcode.com/problem/541/

class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        self.vecs = vecs 
        self.queue = collections.deque([]) 
        for i in range(len(self.vecs)):
            if self.vecs[i]:
                self.queue.append((self.vecs[i][0], i, 0)) 
    """
    @return: An integer
    """
    def _next(self):        
        if self.queue:
            val, list_idx, val_idx = self.queue.popleft()
            if val_idx + 1 < len(self.vecs[list_idx]):
                self.queue.append((self.vecs[list_idx][val_idx + 1], list_idx, val_idx + 1))
            return val

    """
    @return: True if has next
    """
    def hasNext(self):
        return len(self.queue) > 0

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result