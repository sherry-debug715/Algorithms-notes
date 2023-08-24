# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def tree_includes(root, target):
#   if not root:
#     return False
  
#   if root.val == target:
#     return True
  
#   return tree_includes(root.left, target) or tree_includes(root.right, target)


from collections import deque
def tree_includes(root, target):
  if not root:
    return False
  queue = deque( [ root ] )
  
  while queue:
    cur = queue.popleft()
    if cur.val == target:
      return True
    if cur.left:
      queue.append(cur.left)
    if cur.right:
      queue.append(cur.right)
      
  return False
    
    

