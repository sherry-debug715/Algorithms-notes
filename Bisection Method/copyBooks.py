"""
Lintcode problem 437: https://www.lintcode.com/problem/437/
"""

from typing import (
    List,
)

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    """
    edge case:
        if pages is empty or only zeros are stored in pages:
            return 0 
        Logic: the best case is if there is no pages to copy, 0
               the worst case is k = 1 and have to copy every pages from pages list, sum of pages 
               use binary search to find the first num that k people could finish copying.
        start, end = 0, sum of pages
        while start + 1 < end:
            calculate mid 
            if helper(pages, mid) > k:
                end = mid 
            else:
                start = mid 
        
        if helper(pages, start) <= k:
            return start 
        else:
            return end
    """
    # Time: O(nlog(all_pages))
    # Space: O(1)
    def copy_books(self, pages: List[int], k: int) -> int:
        all_pages = sum(pages)
        if not pages or all_pages == 0:
            return 0 
        
        start, end = 0, all_pages
        while start + 1 < end:
            mid = (start + end) // 2 
            if self.people_needed(pages, mid) > k:
                start = mid 
            else:
                end = mid 

        if self.people_needed(pages, start) <= k:
            return start
        return end 
    
    def people_needed(self, pages, limit):
        # num == 4
        people = 0  # 3
        cur_page = limit  # 4
        
        for p in pages:
            if p > limit:
                return float("inf")
            if cur_page + p > limit:
                people += 1 
                cur_page = 0 
            cur_page += p

        return people
