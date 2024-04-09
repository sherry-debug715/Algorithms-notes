# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur_node = dummy

        while l1 or l2:
            list1_val = l1.val if l1 else 0
            list2_val = l2.val if l2 else 0

            two_sum = list1_val + list2_val + carry
            new_carry = two_sum // 10
            val = two_sum % 10 
            cur_node.next = ListNode(val)
            carry = new_carry
            cur_node = cur_node.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # if carry is not 0, cur_node actual value should be greater 
        # than 10, therefore, need to carry over the 1. 
        if carry != 0:
            cur_node.next = ListNode(carry)
        
        return dummy.next