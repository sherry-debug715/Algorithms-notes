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
            if cur_pattern in memo:
                check_word = memo[cur_pattern]
                if check_word != cur_word:
                    return False 
            else:
                if cur_word in used:
                    return used[cur_word] == cur_pattern
                memo[cur_pattern] = cur_word
                used[cur_word] = cur_pattern
            

        return True

