# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  if not root:
    return 0
  
  left_val = tree_sum(root.left)
  right_val = tree_sum(root.right)
  
  return root.val+left_val+right_val