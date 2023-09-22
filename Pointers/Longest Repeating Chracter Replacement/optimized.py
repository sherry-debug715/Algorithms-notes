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

    Initialize a pointer, left, set it to 0 
    Initialize a hash map, cur_window
    Initialize a number, max_length, set it to 0

    For i from 0 to length of s:
        Initialize a a number, window_size, set it to i - left + 1
        document the frequency of s[i] in cur_window 
        Initialize a number, maxFreq, to max(cur_window.values)

        if window_size - maxFreq > k:
            deduct the frequency of cur_sindow[s[L]] by 1 
            L += 1

        update max_length, to max(max_length, i - left + 1)
    return max_length
    """
    def character_replacement(self, s: str, k: int) -> int:
        if not s:
            return 0 
        
        left = 0 
        cur_window = {}
        max_length = 0 

        for i in range(len(s)):
            window_size = i - left + 1
            cur_window[s[i]] = cur_window.get(s[i], 0) + 1 
            maxFreq = max(cur_window.values())
            
            if window_size - maxFreq > k: 
                cur_window[s[left]] -= 1 
                left += 1  
            max_length = max(max_length, i - left + 1) 
            
        
        return max_length
