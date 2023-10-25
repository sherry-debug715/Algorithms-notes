"""
Lintcode problem 902: https://www.lintcode.com/problem/902/description?fromId=161&_from=collection
"""

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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        # write your code here
        if not root:
            return -1 

        stack = []
        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left 
        
        for _ in range(k - 1):
            node = stack[-1]

            if not node.right:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
            else:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        
        return stack[-1].val



