# Lintcode problem 829: https://www.lintcode.com/problem/829/

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def word_pattern_match(self, pattern: str, str: str) -> bool:

        return self.pattern_check(pattern, str, {}, set())
    
    def pattern_check(self, pattern, cur_str, memo, used):
        """
            use memo to document current pattern checking. For example:
            memo = {a: "re", b: "d"}, then when cur_str == "blueredblue" and 
            cur_pattern == a, then cur_str must starts with "re" to match the existing 
            pattern.      
        """
        if not pattern:
            return not cur_str

        cur_pattern = pattern[0]
        if cur_pattern in memo:
            match_str = memo[cur_pattern]
            m = len(match_str)
            if not cur_str.startswith(match_str):
                return False 
            return self.pattern_check(pattern[1:], cur_str[m:], memo, used)

        n = len(cur_str)
        for i in range(1, n + 1):
            prefix = cur_str[:i]
            if prefix in used:
                continue 
            """
            used set is crucial here to maintain the bijection relationship.
            Given a pattern of: "ab", and string of: "redred".
            First Iteration: memo = {"a":"red"}
                             used = {"red"}
            Second Iteration: Attempt to map "b" to "red" is blocked because "red"
                             is already mapped to "a".
            """
            used.add(prefix)
            memo[cur_pattern] = prefix
            if self.pattern_check(pattern[1:], cur_str[len(prefix):], memo, used):
                return True 

            del memo[cur_pattern]
            used.remove(prefix)

        return False 
        
