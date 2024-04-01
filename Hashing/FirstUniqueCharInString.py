# Lintcode problem 209: https://www.lintcode.com/problem/209/?fromId=161&_from=collection

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
# Time: O(N)
# Space: O(N)
    def first_uniq_char(self, str: str) -> str:        
        position = {}
        queue = collections.deque([])

        for l in str:
            if l not in position:
                position[l] = True 
                queue.append(l)
            else:
                position[l] = False 
                while queue and not position[queue[0]]:
                    queue.popleft()
        
        return queue[0]
