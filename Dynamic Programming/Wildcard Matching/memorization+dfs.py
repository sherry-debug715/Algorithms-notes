# Lintcode problem 192: https://www.lintcode.com/problem/192/description?fromId=161&_from=collection

class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    """
    * : for the length of input string, try 1. "", 2. 1 string, 3, 2 string
         4
    cbbba length - sIdx
        3
    c?*a

    """
    def is_match(self, s: str, p: str) -> bool:
        
        return self.check_match(s, p, 0, 0, {})
    
    def check_match(self, s, p, sIdx, pIdx, memo):
        if (sIdx, pIdx) in memo:
            return memo[(sIdx, pIdx)]

        result = False
        # if string is emtpy, pattern should be empty or only "*"
        if sIdx == len(s):
            return self.checkPattern(pIdx, p)
        if pIdx == len(p):
            return sIdx == len(s)

        s_letter = s[sIdx]
        p_letter = p[pIdx] 
        if p_letter != "*":
            first_match = p_letter in ("?", s_letter)
            result = first_match and self.check_match(s, p, sIdx + 1, pIdx + 1, memo) 
        else:
            for idx in range(sIdx, len(s) + 1):
                if self.check_match(s, p, idx, pIdx + 1, memo):
                    return True 

        memo[(sIdx, pIdx)] = result
        return result 
    
    def checkPattern(self, pIdx, pattern):
        while pIdx < len(pattern):
            if pattern[pIdx] != "*":
                return False 
            pIdx += 1
        
        return True



