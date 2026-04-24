class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(i1, i2):
            nums[i1], nums[i2] = nums[i2], nums[i1]
    
        n = len(nums)
        i = 0

        while i < n:
            if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(i, nums[i] - 1)
            else:
                i += 1

        # check the first unsorted one
        for i in range(n):
            val = nums[i]
            i_sort = val - 1
            if nums[i] != i + 1:
                return i + 1

        return n + 1
    