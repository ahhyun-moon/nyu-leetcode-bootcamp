class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # Brute Force: Record any row and col with 0 
        # TC: O(r x c) Space: O(r + c)
        # rows = len(matrix)
        # cols = len(matrix[0])
        # row_zeros = []
        # col_zeros = []
        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             row_zeros.append(i)
        #             col_zeros.append(j)
        # for r in row_zeros:
        #     for j in range(cols):
        #         matrix[r][j] = 0
        # for c in col_zeros:
        #     for i in range(rows):
        #         matrix[i][c] = 0
        # Optimized: 
        # TC: O(r x c) Space: O(1)
        rows = len(matrix)
        cols = len(matrix[0])
        col_zero = False
        for i in range(rows):
            # Check if the first column needs to be converted
            if matrix[i][0] == 0:
                col_zero = True
            # Check other columns/rows need to be converted
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Update elements in the matrix excluding the first row and column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Check if the first row needs to be converted
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0
        # Check if the first column needs to be converted
        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0