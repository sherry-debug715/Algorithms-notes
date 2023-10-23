"""
Lintcode problem 578: https://www.lintcode.com/problem/578
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        a_exist, b_exist, lca = self.findLca(root, A, B)
        if a_exist and b_exist:
            return lca 
    
    def findLca(self, root, A, B):
        if not root:
            return False, False, None 

        left_a, left_b, rootA = self.findLca(root.left, A, B)
        right_a, right_b, rootB = self.findLca(root.right, A, B)

        a_exist = left_a or right_a or root == A
        b_exist = left_b or right_b or root == B 

        if root == A or root == B:
            return a_exist, b_exist, root 
        
        if rootA and rootB:
            return a_exist, b_exist, root 
        if rootA:
            return a_exist, b_exist, rootA 
        if rootB:
            return a_exist, b_exist, rootB
        
        return False, False, None

