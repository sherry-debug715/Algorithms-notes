from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    """
    Insertion sort:
    function sort_integers:
        Iterate over list a, using i, starting from 1.
            if i doesn't go over the edge and a[i] >= a[i - 1]: 
                continue

            insertion(i, a)
        
        return a
    
    function insertion(i, a):
        WHILE i > 0:
            if a[i] < a[i - 1]:
                swap 
            i -= 1    
    """
    def sort_integers(self, a: List[int]):
        for i in range(1, len(a)):
            if i < len(a) and a[i] >= a[i - 1]:
                continue

            self.insertion(i, a) 
        
        return a 
    
    def insertion(self, index, a):
        while index > 0:
            if index > 0 and a[index] < a[index - 1]:
                a[index], a[index - 1] = a[index - 1], a[index]
            index -= 1
