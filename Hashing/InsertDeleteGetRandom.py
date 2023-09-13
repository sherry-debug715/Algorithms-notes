"""
Lintcode problem 657: https://www.lintcode.com/problem/657/?fromId=161&_from=collection
"""

import random
class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.values = []
        self.keys = {}
    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val in self.keys:
            return False 
        self.keys[val] = len(self.values)
        self.values.append(val)
        return True
    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.keys:
            return False
        # swap the deleted val with the last element from values list first, to maintain correctness of 
        # indexes of other val.
        index, last_val = self.keys[val], self.values[-1]
        self.values[index], self.values[-1] = last_val, val
        self.values.pop() 
        del self.keys[val]
        # update index for last_val in the hash map 
        self.keys[last_val] = index  
        return True
    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        if not self.values:
            return False 
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()