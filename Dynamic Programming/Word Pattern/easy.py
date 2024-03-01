# leetcode problem 290: https://leetcode.com/problems/word-pattern/description/

# Time: O(N)
# Space: O(N)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern:
            return not s 
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        memo = {} 
        used = {}

        for i in range(len(pattern)):
            cur_word = words[i]                
            cur_pattern = pattern[i]
            if cur_pattern in memo and memo[cur_pattern] != cur_word:
                return False 
            if cur_word in used and used[cur_word] != cur_pattern:
                return False
            memo[cur_pattern] = cur_word
            used[cur_word] = cur_pattern
            
        return True

from itertools import zip_longest
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split()
        return len(set(pattern)) == len(set(word_list)) == len(set(zip_longest(word_list, pattern)))
        

