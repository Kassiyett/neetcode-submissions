class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        1, 2, 3
        4, 0, 5
        6, 7, 8

        1, 2, 3
        0, 0, 0
        6, 7, 8       
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # find 0, store (r, c)
        zeros = []
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeros.append((r, c))
        # change 
        for r, c in zeros:
            # change row
            for i in range(cols):
                matrix[r][i] = 0
            # change col
            for i in range(rows):
                matrix[i][c] = 0
            