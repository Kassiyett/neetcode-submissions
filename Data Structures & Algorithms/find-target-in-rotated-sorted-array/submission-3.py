class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            # BS
            print(nums[l], nums[m], nums[r])
            if nums[m] == target:
                return m
            # left side is if alredy sorted
            if nums[l] <= nums[m]:
                if nums [l] <= target <= nums[m]:
                    r = m - 1
                    print(l, r)
                else:
                    l = m + 1
            # right side is sorted
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
