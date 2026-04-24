class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            # left side is smaller, so search there
            if nums[m] >= nums[r]:
                l = m + 1
            # right side is sorted 
            else:
                r = m
        return nums[l]