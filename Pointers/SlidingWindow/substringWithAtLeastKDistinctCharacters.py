# Lintcode problem 1375: https://www.lintcode.com/problem/1375/description?fromId=161&_from=collection

class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
     l 
    "abaabcabcabc"
           i
    {a: 3, b: 2, c: 1}
    1

    """
    def k_distinct_characters(self, s: str, k: int) -> int:


        total = 0
        counter ={}
        n = len(s)
        left = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while left <= right and len(counter)>=k:
				#每次挪动left都需要加上n-right, 因为从窗口已凑够了k个数开始，s[right:]中的
                # 每一个数都可以和s[left:right]substring组成一个合规的substring. 
                total += n -right
                counter[s[left]] -= 1 
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left +=1        
        return total


