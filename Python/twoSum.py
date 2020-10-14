class Map_Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for i in range(len(nums)):
            if ((target - nums[i]) in nums_dict.keys()):
                return [i, nums_dict.get(target - nums[i])]
            nums_dict[nums[i]] = i