# Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

# You may assume that the input list is non-empty.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def is_univalue_list(head, prev=None):
#   if head is None:
#     return True
  
#   if head is not None and prev is not None and head.val != prev.val:
#     return False
  
#   return is_univalue_list(head.next, head)

# def is_univalue_list(head, prev=None):
#   if head is None:
#     return True
  
#   if prev is None or prev.val == head.val:
#     return is_univalue_list(head.next, head)
  
#   return False


def is_univalue_list(head):
  current = head
  while current is not None:
    if current.val != head.val:
      return False    
    current = current.next
  
  return True


# def is_univalue_list(head):
#   value = set()
#   value.add(head.val)
  
#   current = head.next
#   while current:
#     if current.val not in value:
#       return False
#     current = current.next
  
#   return True

def is_univalue_list(head):
  if head is None:
    return True
  
  next = head.next
  if next is None:
    return True
  if head.val != next.val:
    return False
  return is_univalue_list(head.next)

def is_univalue_list(head):
  return helper(head, head.val)

def helper(head, prev):
  if not head:
    return True

  if head.val != prev:
    return False
  
  return helper(head.next, head.val)
    
  
a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 4

print(is_univalue_list(a)) # False