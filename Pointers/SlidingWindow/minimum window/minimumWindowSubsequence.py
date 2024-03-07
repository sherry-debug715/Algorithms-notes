# Lintcode problem 857: https://www.lintcode.com/problem/857/

class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the minimum substring of S
    """
    # Time: O(m * n) where m is len(t) and n is len(s)
    # Space: O(n)
    def min_window(self, s: str, t: str) -> str:
        # use a list to document the index of t[0] from input s
        cur = [idx if val == t[0] else None for idx, val in enumerate(s)]
        # [None, 1, None, None, None, 5, None, None, None]

        for j in range(1, len(t)):
        # last will always reference the index of closest t[0] in the current substring
            last = None 
        # new[index] index of t[0] of current substring, where index is the index of t[j] from input s
            new = [None] * len(s)

            for idx, val in enumerate(s):
                if last is not None and val == t[j]:
                    # index of new list document the location of t[j] from s
                    # and new[idx] is the begining index of t[0] of the current substring
                    new[idx] = last
                # no need to check if last is None, we need to update last for new substrings
                if cur[idx] is not None:
                    last = cur[idx]
                # if last is not None, that means we have found at least one possible substring that
                # begins with t[0] 
            cur = new
        
        ans = (0, len(s))
        # print("cur", cur)
        for idx, val in enumerate(cur):
            """
            it's important to check if idx - val + 1 > 1.
            for example:
                s = "cnhczmccqouqadqtmjjzl"
                t = "mm"
            cur = [None, None, None, None, None, 5, None, None, None, None, None, None, None, None, None, None, 5, None, None, None, None]
            when index == 5, because the last letter from t is also "m", therefore, cur[5] is only referencing one letter instead of two.
            """
            if val is not None and idx - val + 1 > 1 and idx - val + 1 < ans[1] - ans[0]:
                ans = (val, idx + 1) 
        begin, end = ans[0], ans[1]
        # print("begin, end", begin, end)
        return s[begin: end] if s and end < len(s) else ""