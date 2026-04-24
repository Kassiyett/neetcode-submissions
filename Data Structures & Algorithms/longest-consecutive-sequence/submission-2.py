class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                consecutive_nums = 1
                while num + 1 in numsSet:
                    consecutive_nums += 1
                    num = num + 1
                result = max(result, consecutive_nums)

        return result
