"""
LintCode problem 386: https://www.lintcode.com/problem/386/
"""
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    """
    Edge case:
    1. if s is empty, return 0
    2. if k == 0, return 0 

    Initialize a dictionary, cur_window.
    Initialize a pointer, j, set it to 0
    Initialize a number, max_sub, set it to 0
    Iterate from 0 to length of s, with i:
            add each ele to cur_window
            while there are more than k distinct characters, keep sliding window:
                reduce the frequency of the character at j, if it's 0, remove it.
                j += 1
            
            max_sub = max of i - j + 1 to old max_sub
    return max_sub
    """
    # Time: O(n)
    # Space: O(n)
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0 
        
        cur_window = {}
        j = 0
        max_sub = 0 
        for i in range(len(s)):
            cur_window[s[i]] = cur_window.get(s[i], 0) + 1 
# Slide the window when there are more than k distinct characters
            while len(cur_window) > k:
                if cur_window[s[j]] > 1:
                    cur_window[s[j]] -= 1 
                else:
                    del cur_window[s[j]]
                j += 1 

            max_sub = max(max_sub, i - j + 1) 
        return max_sub
        

