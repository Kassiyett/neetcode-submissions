class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        height = [1,7,2,5,4,7,3,6]
        1,7: 1*1
        7,2: 2
        7,2,5: 5*2 = 10
        7,2,5,4,7: 7*5 = 35
        7,2,5,4,7,3,6: 6 * 6 = 36

        [1,7,2,5,4,7,3,6]
        1,7,2,5,4,7,3,6: 1*7 = 7, -> 1<6: so move l++
        7,2,5,4,7,3,6: 36 -> 7>6 so move r++

        1, 5, 2, 3
        """
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            left = heights[l]
            right = heights[r]
            currArea = min(left, right) * (r-l)
            # print(left, right, currArea)
            maxArea = max(currArea, maxArea)
            if left < right:
                l += 1
            else:
                r -= 1
        return maxArea