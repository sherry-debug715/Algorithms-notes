# Lintcode problem 70: https://www.lintcode.com/problem/70/description?fromId=161&_from=collection

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
from collections import deque
class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def level_order_bottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        output = deque()
        while queue:
            cur_path = []
            for i in range(len(queue)):
                cur = queue.popleft()
                cur_path.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right) 
            output.appendleft(cur_path)

        return list(output)

        
        