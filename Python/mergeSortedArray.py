class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1.pop()
        nums1_it = 0
        for num in nums1:
            if nums2 == []:
                return
            if nums2[0] <= nums1[nums1_it]:
                nums1.insert(nums1_it, nums2[0])
                nums2.remove(nums2[0])
            nums1_it += 1
        nums1.extend(nums2)
        return