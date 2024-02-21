# Lintcode problem 171: https://www.lintcode.com/problem/171/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
             we will sort your return value in output
    """
    """
        Edge case:
            if strs is empty:
                return []
        Code:
            helper function, get_key, returns a 2-D tuple with letter and quantity 
                from a given string
            initialize a dictionary, tracker, {}
            iterate over strs with word:
                ele_counter = self.get_key(strs)
                tracker[ele_counter] = tracker.get(ele_counter, []) or add 
            return [val for wordList in tracker.values() for val in wordList]
    """
    # Time: O(m * n) where m is the length of strs and n is the length of each str from strs.
    # Space: O(n)
    def anagrams(self, strs: List[str]) -> List[str]:
        tracker = collections.defaultdict(list) # O(1)

        for word in strs: # O(n)
            key = self.get_key(word) # O(N)
            tracker[key].append(word)
        
        return [val for wordList in tracker.values() for val in wordList if len(wordList) > 1]
            
        
    
    def get_key(self, word):
        count = [0] * 26
        for l in word:
            count[ord(l) - ord("a")] += 1
        return tuple(count)


