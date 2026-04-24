class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            val = nums[i]
            # if negative or out of range, skip
            if val <= 0 or val > n:
                i += 1
                continue

            index = val - 1
            # swap if index of val is not val - 1
            if val != nums[index]:
                nums[i] = nums[index]
                nums[index] = val
            # if it is on its place, just skip
            else:
                i += 1
        # check if val != i + 1, if not return val - 1
        for i in range(n):
            val = nums[i]
            if val != i + 1:
                return i + 1
        return n + 1