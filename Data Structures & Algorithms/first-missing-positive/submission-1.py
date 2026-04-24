class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        [-2, -1, 0]
        1
        [1, 2, 4]
        3
        """
        nums.sort()
        result = 1

        # get min positive

        for num in nums:
            if num == result:
                result = result + 1
            
        return result