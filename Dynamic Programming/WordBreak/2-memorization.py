# Lintcode problem 582: https://www.lintcode.com/problem/582/

from typing import (
    List,
    Set,
)

class Solution:
    """
    @param s: A string
    @param word_dict: A set of words.
    @return: All possible sentences.
             we will sort your return value in output
        i
    lintcode
    """
    def word_break(self, s: str, word_dict: Set[str]) -> List[str]:
        if not s or not word_dict:
            return []

        return self.dfs(s, word_dict, {})
    
    def dfs(self, s, word_dict, memo):
       # memo[s] references a list of output of substring of s
        if s in memo:
            return memo[s] 
        
        if len(s) == 0:
            return [] 
        
        sentences = []
        for i in range(1, len(s) + 1):             
            word = s[:i]
            if word not in word_dict:
                continue 
            rest_sentences = self.dfs(s[i:], word_dict, memo)
            for sub_str in rest_sentences:
                sentences.append(word + " " + sub_str)
                
        # Input s could also be found in wordDict
        if s in word_dict:
            sentences.append(s)

        memo[s] = sentences 
        return sentences

