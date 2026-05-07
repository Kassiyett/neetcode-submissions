class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topLeft = matrix[top][l + i]

                # topleft = bottomleft
                matrix[top][l + i] = matrix[bottom - i][l]
                # bottomleft - bottomright
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # bottomright - topright
                matrix[bottom][r - i] = matrix[top + i][r]
                # topright - topleft
                matrix[top + i][r] = topLeft 
                
            l += 1
            r -= 1