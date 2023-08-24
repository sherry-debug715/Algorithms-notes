# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def tree_min_value(root):
#   if root is None:
#     return float('inf')
    
#   left = tree_min_value(root.left)
  
#   right = tree_min_value(root.right)

#   return min(root.val, left, right)

from collections import deque
def tree_min_value(root):
  queue = deque( [ root ] )
  min = root.val
  
  while queue:
    cur = queue.popleft()
    if cur.val < min:
      min = cur.val
    
    if cur.left:
      queue.append(cur.left)
    if cur.right:
      queue.append(cur.right)
  return min
      

    
  