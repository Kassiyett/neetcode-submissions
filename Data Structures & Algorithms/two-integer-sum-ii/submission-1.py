class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        res = []

        while l < r:
            sumVal = numbers[l] + numbers[r]
            if sumVal > target:
                r -= 1
            if sumVal < target:
                l +=1
            if sumVal == target:
                return [l+1, r+1]
        return res