"""
Lintcode problem 1246: https://www.lintcode.com/problem/1246/
"""

class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    """
    Edge case:
    1. if s is empty, return 0 

    Initialize a pointer, j, set it to 0 
    Initialize a number, max_frequent, set it to 0
    Initialize a hash map, cur_window
    Initialize a number, res, set it to 0.

    For i from 0 to length of s:
        While j < length of s and within the current window, the size of window - max_frequent <= k:
            document the frequency of s[j] in cur_window 
            update max_frequent
            update res with max(res, j - i + 1)
            j += 1 
        
        check if window size - max_frequent > k:
            deduct s[i] from hash map
            continue 

    return res
    """
    def character_replacement(self, s: str, k: int) -> int:
        # print("s",s)
        # print("k", k)
        if not s:
            return 0 
        
        j = 0 
        max_frequent = 0 
        cur_window = {}
        res = 0 

        for i in range(len(s)):
            while j < len(s) and j - i - max_frequent <= k:
                cur_window[s[j]] = cur_window.get(s[j], 0) + 1 
                max_frequent = max(max_frequent, cur_window[s[j]])
                j += 1 
            
            if j - i - max_frequent > k: 
                cur_window[s[i]] -= 1 
                res = max(res, j - i - 1) 
            else:
                res = max(res, j - i) 
            
            max_frequent = max(cur_window.values()) 
        
        return res
