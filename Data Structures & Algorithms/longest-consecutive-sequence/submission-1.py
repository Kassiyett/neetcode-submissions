class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force
        # nums = set(nums)
        # res = 0
        # for n1 in nums:
        #     streak = 0
        #     curr = n1
        #     while curr in nums:
        #         streak += 1
        #         curr += 1
        #     res = max(streak, res)
        # return res


        # Optimal Solution
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:
                length = 1
                while n + length in nums:
                    length += 1
                res = max(length, res)
        return res