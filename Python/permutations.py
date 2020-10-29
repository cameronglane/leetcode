class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        def dfs(l):
            if l == n-1:
                res.append(list(nums))
                return 
            for i in range(l, n):
                nums[l], nums[i] = nums[i], nums[l]   # swap nums[l] and nums[i]
                dfs(l+1)
                nums[l], nums[i] = nums[i], nums[l]  # swap them back
        dfs(0)
        return res