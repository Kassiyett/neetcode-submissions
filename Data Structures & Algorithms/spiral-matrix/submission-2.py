class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        1, 2, 3
        4, 5, 6
        7, 8, 9

        1 2 3 6 9 7 8 4 5
        """
        top, bottom = 0, len(matrix) 
        l, r = 0, len(matrix[0])
        res = []

        while l < r and top < bottom:
            # getting top row
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1
            
            # getting right column
            for i in range(top, bottom): 
                res.append(matrix[i][r - 1])
            r -=1

            if not (l < r and top < bottom):
                break

            # bottom row
            for i in range(r - 1, l - 1, -1): # 1, -1: 1, 0
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # left col
            for i in range(bottom - 1, top - 1, -1): 
                res.append(matrix[i][l])
            l += 1

        return res
                