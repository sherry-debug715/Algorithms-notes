# Lintcode problem 74: https://www.lintcode.com/problem/74/?fromId=161&_from=collection

#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    # 当一个版本为正确版本，则该版本之前的所有版本均为正确版本
    def findFirstBadVersion(self, n):
        l, r = 1, n
        while l + 1 < r:
            mid = (l + r) // 2
            if SVNRepo.isBadVersion(mid):
                r = mid
            else:
                l = mid
        
        if SVNRepo.isBadVersion(l):
            return l
        return r