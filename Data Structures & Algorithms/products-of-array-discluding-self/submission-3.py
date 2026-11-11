class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]
        [1, 1, 1, 1]
        1*2*4*6 = 8*6 = 48
        [48, 24, 12, 8]

        [-1,0,1,2,3]
         [1,1,1,1,1]
        withoutZero = -1*1*2*3 = -6
        isThereZero = True
        zeroCount = 1

        [None]*len(nums)
        [0, -6, 0, 0, 3]
        withoutZero = -1*1*2*3 = -6
        isThereZero = True
        zerCount = 2

        [-1,0,1,0,3]
        
        keep three variables: withoutZero, isThereZero, zerCount
        if zeroCount == 1
        then 0 for all, if 0 then withoutZero
        if zeroCount > 1
        then 0 for all
        """
        withoutZero = 1
        zeroCount = 0
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                withoutZero *= n

        for i in range(len(nums)):
            curr = nums[i]
            if zeroCount == 1:
                if curr == 0:
                    nums[i] = withoutZero
                else:
                    nums[i] = 0

            if zeroCount > 1:
                nums[i] = 0

            if zeroCount == 0:
                nums[i] = withoutZero // curr
        
        return nums