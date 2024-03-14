# Lintcode problem 155: https://www.lintcode.com/problem/155/description?fromId=161&_from=collection

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
    @param root: The root of binary tree
    @return: An integer
    """
    def min_depth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = collections.deque([(root, 1)])

        while queue:
            cur, depth = queue.popleft()
            if cur.left is None and cur.right is None:
                return depth
            if cur.left:
                queue.append((cur.left, depth + 1))
            if cur.right:
                queue.append((cur.right, depth + 1))
        
        return 0
