class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        subset = []

        def dfs(i):
            print("this is how subset looks like", subset)
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            print("first run")
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            print("second run and this is i", i)
            dfs(i + 1)

        dfs(0)
        return res

# root node (dfs(0), subset=[])
# ├── include 1 (dfs(1), subset=[1])
# │   ├── include 2 (dfs(2), subset=[1,2]) -> return subset [1,2]
# │   └── exclude 2 (dfs(2), subset=[1]) -> return subset [1]
# └── exclude 1 (dfs(1), subset=[])
#     ├── include 2 (dfs(2), subset=[2]) -> return subset [2]
#     └── exclude 2 (dfs(2), subset=[]) -> return subset []