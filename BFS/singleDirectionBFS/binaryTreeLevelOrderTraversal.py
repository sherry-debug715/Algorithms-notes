"""
Lintcode problem 69: https://www.lintcode.com/problem/69/
"""

from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if not root:
            return []

        queue = collections.deque([root, None])
        res = []
        level = []

        while queue:
            cur = queue.popleft()
            if cur is None:
                if queue:
                    queue.append(None) 
                res.append(level)
                level = []
                continue 
            level.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right) 
        
        return res 
            
            
