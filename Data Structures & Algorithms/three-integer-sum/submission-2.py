class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        length = len(nums)
        """
        [-2,0,0,2,2]
        -2: t = - + 2 + -1 = 0
        """
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l = i + 1
            r = length - 1
            while l < r:
                threesum = nums[l] + nums[r] + n
                print(threesum)
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    if l > 0 and nums[l] == nums[l-1]:
                        l += 1
                    if nums[r] == nums[r+1]:
                        r -= 1
        return res
                
            