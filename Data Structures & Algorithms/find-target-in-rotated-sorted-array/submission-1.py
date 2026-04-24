class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if already sorted
        """
        3,4,5,6,1,2 # 4
        1 < 6, 1 < 3: go right
        

        """
        l, r = 0, len(nums)-1

        while l <= r:
            # if sorted, normal bin search

            m = (l+r)//2
            print(nums[l], nums[m], nums[r])
            
            if nums[m] == target:
                return m
            # left is sorted
            elif nums[l] <= nums[m]:
                # check if target is within
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right is sorted
            elif nums[r] >= nums[m]:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m -1
        
        return -1

