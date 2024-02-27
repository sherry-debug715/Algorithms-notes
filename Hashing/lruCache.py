#Lintcode problem 134: https://www.lintcode.com/problem/134/?fromId=161&_from=collection

class Node:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_prev = {}
        self.dummy = Node()
        self.tail = self.dummy

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # check if key is not in cache
        if key not in self.key_to_prev:
            return -1
        # get the prev node by key
        prev = self.key_to_prev[key]
        cur_node = prev.next
        # move the cur_node to the tail position
        self.swap(prev)
        return cur_node.val
    
    def swap(self, prev):
        cur_node = prev.next
        if cur_node == self.tail:
            return
        # remove the current node from linked list
        prev.next = cur_node.next
        # update cur_node.key prev to prev
        self.key_to_prev[cur_node.next.key] = prev 
        cur_node.next = None
        self.add_to_tail(cur_node.key, cur_node.val)
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.key_to_prev:
            self.swap(self.key_to_prev[key])
            self.tail.val = value
            return
        self.add_to_tail(key, value)
        if len(self.key_to_prev.values()) > self.capacity:
            self.pop_front()
    
    def pop_front(self):
        # 1. reset the old head.next.prev to dummy
        # 2. delete old head key in self.capacity
        # 3. set dummy.next to old head.next 
        old_head = self.dummy.next
        self.key_to_prev[old_head.next.key] = self.dummy
        del self.key_to_prev[old_head.key]
        self.dummy.next = old_head.next
        
    
    def add_to_tail(self, key, val):
        # set the prev node of the key to the old tail 
        self.key_to_prev[key] = self.tail 
        # add to the tail of the linked list 
        node = Node(key, val)
        self.tail.next = node
        self.tail = node


