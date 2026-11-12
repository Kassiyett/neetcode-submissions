class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [3,4,5,6,1,2] 1
        sorted, unsorted
        mid = 2 

        right side sorted:
        [6,1,2,3,4,5] 4: compare mid<right and mid<target < right, do binary search there
        3,4,5: mid<right and target == mid, return mid
        
        [6,1,2,3,4,5] 1: compare mid<right and target < mid, then search left
        6,1,2: return target

        left side sorted
        [2,3,4,5,6,1] 1: mid>right and left>target, search right
        5,6,1: mid>right and left>target, search right
        return 1

        [2,3,4,5,6,1] 3: mid>right and left<target<mid, search right: do binary search there

        if left side sorted:
            and if left<target<mid
                binary search from left
        if right side sorted
            and if mid<target < righ
                binary search from right
        """
        # for i, num in enumerate(nums):
        #     if num == target:
        #         return i

        l, r = 0, len(nums)-1
        # [4,5,6,7,0,1,2] 0
        while l <= r:
            m = (l+r) // 2
            left, mid, right = nums[l], nums[m], nums[r]
            print(left, mid, right)
            if mid == target:
                return m
            if mid<right: # right side sorted
                if mid<=target <= right:
                    l = m+1
                else:
                    r = m
            else: # left side sorted
                if left<=target<=mid:
                    r = m
                else:
                    l = m+1

        return -1
