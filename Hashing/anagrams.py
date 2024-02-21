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
            helper function, get_key, returns tuple.
            initialize a dictionary, tracker, set it's default value as list structure
            iterate over strs with word:
                get key from self.get_key(word)
                add word to tracker[key] if key in tracker.
            return: only sub-lists with length greater than one sould be considered.
    """
    # Time: O(m * n) where m is the length of strs and n is the length of each str from strs.
    # Space: O(n)
    def anagrams(self, strs: List[str]) -> List[str]:
        tracker = collections.defaultdict(list) # O(1)

        for word in strs: # O(M)
            key = self.get_key(word) # O(N)
            tracker[key].append(word)
        
        return [val for wordList in tracker.values() for val in wordList if len(wordList) > 1]
            
        
    
    def get_key(self, word):
        count = [0] * 26
        for l in word:
            count[ord(l) - ord("a")] += 1
        return tuple(count)


