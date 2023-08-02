# Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

# Do this in-place.

# You may assume that the input list is non-empty.

# You may assume that the input list contains the target.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


# return the new head 
# def remove_node(head, target_val):
#   # if the head is the target val
#   if head.val == target_val:
#     return head.next
  
#   prev = None
#   current = head
  
#   while current is not None:
#     if current.val == target_val:
#       prev.next = current.next
#       return head
      
#     prev = current
#     current = current.next

def remove_node(head, target_val):
  # empty linked list
  if head is None:
    return None
  
  #  if target node find, return the targetNode.next
  if head.val == target_val:
    return head.next
  
  head.next = remove_node(head.next, target_val)
  
  return head
  
  
