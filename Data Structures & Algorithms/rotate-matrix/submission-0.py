class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        1 2 3
        4 5 6
        7 8 9


        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                print(l, r, i)
                topLeft = matrix[top][l + i]
                topRight = matrix[top + i][r]
                bottomLeft = matrix[bottom - i][l]
                bottomRight = matrix[bottom][r - i]
                print(topLeft, topRight, bottomRight, bottomLeft)

                matrix[top + i][r] = topLeft
                matrix[bottom][r - i] = topRight
                matrix[bottom - i][l] = bottomRight
                matrix[top][l + i] = bottomLeft

            l += 1
            r -= 1