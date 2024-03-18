"""
Lintcode problem 68: https://www.lintcode.com/problem/68/
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result 
        
        prev, stack = None, [root] 

        while stack:
            cur = stack[-1] 
            # traverse down current branch 
            if not prev or prev.left == cur or prev.right == cur:
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right) 
            # once the left child node is added to the result, check if there is a 
            # right child 
            elif cur.left == prev:
                if cur.right:
                    stack.append(cur.right) 
            else:
                result.append(cur.val)
                stack.pop() 
            
            prev = cur 
        
        return result 
