class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # creating memo that have [None, None] for the length of the arr
        l = 0
        r = 0
        prefix = 0
        s = 0
        maxSum = float("-inf")

        while r < len(nums):
            prefix += nums[r]
            maxSum = max(prefix, maxSum)
            if prefix < 0:
                prefix = 0
                l = r
            r += 1

        return maxSum