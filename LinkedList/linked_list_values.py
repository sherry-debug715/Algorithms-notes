


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def linked_list_values(head):
#   linked_list = []
  
#   current = head
#   while current is not None:
#     linked_list.append(current.val)
#     current = current.next
#   return linked_list

# def linked_list_values(head, linked_list=[]):
#   if head is None:
#     return linked_list
#   linked_list.append(head.val)
#   return linked_list_values(head.next, linked_list)

# def linked_list_values(head, linked_list=[]):
#   if head is None:
#     return linked_list
#   return linked_list_values(head.next, [*linked_list, head.val])

def linked_list_values(head):
  if head is None:
    return []
  return [head.val, *linked_list_values(head.next)]



    
