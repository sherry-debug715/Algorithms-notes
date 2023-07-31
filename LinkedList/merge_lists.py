# Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty and contain increasing sorted numbers.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


# def merge_lists(head_1, head_2):
#   dummy_head = Node(None)
#   tail = dummy_head
#   cur_1 = head_1
#   cur_2 = head_2
  
#   while cur_1 is not None and cur_2 is not None:
#     if cur_1.val < cur_2.val:
#       tail.next = cur_1
#       tail = cur_1
#       cur_1 = cur_1.next
#     else:
#       tail.next = cur_2
#       tail = cur_2
#       cur_2 = cur_2.next
  
#   if cur_1 is None:
#     tail.next = cur_2
#   if cur_2 is None:
#     tail.next = cur_1
    
#   return dummy_head.next

def merge_lists(head_1, head_2):
  # empty linked list 
  if head_1 is None and head_2 is None:
    return None
  
  # if head_1 linked list is shorter
  if head_1 is None:
    return head_2
  # if head_2 linked list is shorter
  if head_2 is None:
    return head_1
  
  # compare value to form new sorted linked list 
  if head_1.val < head_2.val:
    head1_next = head_1.next
    head_1.next = merge_lists(head1_next, head_2)
    return head_1
  
  else:
    head2_next = head_2.next
    head_2.next = merge_lists(head_1, head2_next)
    return head_2
  