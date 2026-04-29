class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        [1, 2, 3, 6, 9, 8, 7, 4, 5]

        res = [1, 2, 3]
        mat = [[6, 9], [5, 8], [4, 7]]
        res = [1, 2, 3, 6, 9]
        mat = [[8, 7], [5, 4]]
        """
        # go over first round - add to res
        # transpose the matrix
        # reverse rows - to 90
        # top row will be the exact one

        res = []
        while matrix:
            res += matrix.pop(0)
            transList = list(zip(*matrix))
            matrix = transList[::-1]
        
        return res