class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
       3,4,5,6,1,2

        """
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            # if it is sorted already
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (r+l)//2
            res = min(res, nums[m])
            print(nums[l], nums[r], nums[m])
            # l = 2, r = 1, m = 2
            # if left is sorted, go right.
            if nums[l] <= nums[m]:
                l = m + 1
            # search left
            else:
                r = m
        return res