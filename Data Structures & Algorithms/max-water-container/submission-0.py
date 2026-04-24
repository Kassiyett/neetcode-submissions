class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [1,7,2,5,4,7,3,6]
        7, 6: area = (7-1) * 6 = 36

        1: area = 7 * 1 = 7   6 > 1 : l++
        7: area = 36 6 < 7 r++

        area = diff indes * min(height)

        how to find 7, 6?
        left, right pointers?
        how to update them?
        keep track of max area? and if it is larger, then update, if it is lower then update?
        """
        max_area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, area)
            if heights[l] > heights[r]:
                r-= 1
            elif heights[l] < heights[r]:
                l+=1
            else:
                r-=1
                l+=1
        return max_area
