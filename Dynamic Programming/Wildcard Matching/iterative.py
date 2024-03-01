# this solution beats 99.8% submissions

class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    """
    starIdx, sTmpIdx = 9, 11
                 s
    "acaabbaccbbacaabbbb"
                p
    "a*?*b*?*a*aa*a*"
    """
    def is_match(self, s: str, p: str) -> bool:
        str_pointer, p_pointer = 0, 0
        starIdx, tempStr_pointer = -1, -1 

        while str_pointer < len(s):
            if p_pointer < len(p) and (s[str_pointer] == p[p_pointer] or p[p_pointer] == "?"):
                str_pointer += 1
                p_pointer += 1
            elif p_pointer < len(p) and p[p_pointer] == "*":
                starIdx = p_pointer
                tempStr_pointer = str_pointer
                p_pointer += 1
            elif starIdx != -1:
                p_pointer = starIdx + 1
                tempStr_pointer += 1
                str_pointer = tempStr_pointer
            else:
                return False
        
        while p_pointer < len(p):
            if p[p_pointer] != "*":
                return False 
            p_pointer += 1
        return True
