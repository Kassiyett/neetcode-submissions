class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        3,4,5,6,1,2  m = 5
        3 > 2 search right
        6,1,2 m = 1 6 > 2 -> search right
        m = 2 

        [4,5,6,1,2,3] 4>3 search right 
        1,2,3 1 < 3 seach left

        1,2,3 -> search left
        3,1,2 -> search right
        2,3,1 -> search right

        5,1,2,3,4 search right, doestn work
        5,1,2,3,4 2 < 4, search left

        4,5,1,2,3 -> 1 < 3 search left
        4,5,1 -> 5>1 search right
        1
        """
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        minNum = float('inf')
        while l<r:
            m = (l + r) // 2
            mid = nums[m]
            left = nums[l] #2
            right = nums[r] # 1
            # minNum = min(minNum, mid) # 2
            if mid > right: # 
                l = m+1
            else: # right side is smaller, search there
                r = m
            
        return nums[l]

            