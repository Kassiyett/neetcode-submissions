class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        3, 4, 5, 6
        7 - 3
        4
        if 4 in 3 
        then return index of it + key of the complecent
        """
        complecents = defaultdict(int) # complecent: index
        result = [-1, -1]

        for i, num in enumerate(nums):
            if num in complecents:
                return [complecents[num], i]
            complecent = target - num
            complecents[complecent] = i
        
        return result