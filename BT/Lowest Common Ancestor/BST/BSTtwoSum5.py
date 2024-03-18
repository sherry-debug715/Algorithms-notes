# Lintcode problem 689: https://www.lintcode.com/problem/689/

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        if not root:
            return None
        
        visited = set()
        queue = collections.deque([root]) 

        while queue:
            cur = queue.popleft()
            diff = n - cur.val 
            if diff in visited:
                return [diff, cur.val] 
            visited.add(cur.val) 
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right) 
        
        return None