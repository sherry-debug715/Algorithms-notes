# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# given linked list is already sorted
# remove dups from the linked list
# in place
def removeDuplicatesFromLinkedList(linkedList):
    cur = linkedList
    next = cur.next
    while next:
        if cur.value == next.value:
            next = next.next
            continue
        cur.next = next
        cur = next
        next = next.next
    # if we have a situation where the last 2 nodes have the same value
    # cur       next
    # 6 -> 6 -> None
    # we will break out of the while loop with cur still pointing at duplicated node 6.
    if cur.next is not None:
        cur.next = None
    return linkedList