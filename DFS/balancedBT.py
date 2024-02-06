# Lintcode problem 93: https://www.lintcode.com/problem/93/description

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
# Time Complexity: O(N). For an unbalanced tree, the code stops when the difference between two subtree is greater than one. Worst case is when we the tree is balanced, which necessitates traversing through the entire tree.

# Space Complexity: O(H), where H is the height of the tree. For a balanced tree, the space complexity is O(logN). Worst case, singly linked list, O(N) 
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        # write your code here
        if not root:
            return True 
        
        def dfs(root):
            if not root:
                return True, 0 
            
            is_left_balanced, left_level = dfs(root.left) 
            is_right_balanced, right_level = dfs(root.right) 

            cur_level = max(left_level, right_level) + 1

            if not is_left_balanced or not is_right_balanced:
                return False, cur_level 
            if abs(right_level - left_level) > 1:
                return False, cur_level 
            
            return True, cur_level 
        
        is_balanced, _ = dfs(root)
        return is_balanced