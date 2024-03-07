# Leetcode problem 76: https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    """
    t = {a: 2}
    w = {a: 1}
    need = 1
    have = 1
       l
    ""aa""
       r
    """
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        t_map, window = {}, {}
        min_len = float("inf")
        len_idx = (0, 0)

        for l in t:
            t_map[l] = t_map.get(l, 0) + 1
            window[l] = 0 

        need = len(t_map)
        have = 0
        
        l = 0
        for r in range(len(s)):
            if s[r] not in window:
                continue 
            window[s[r]] += 1
            if window[s[r]] == t_map[s[r]]:
                have += 1
            while need == have:
                cur_len = r - l + 1
                if cur_len < min_len:
                    min_len = cur_len
                    len_idx = (l, r + 1)
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < t_map[s[l]]:
                        have -= 1
                l += 1
        
        if min_len == float("inf"):
            return ""

        return s[len_idx[0]: len_idx[1]]


        
        