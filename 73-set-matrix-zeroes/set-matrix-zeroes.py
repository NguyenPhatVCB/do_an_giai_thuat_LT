class Solution:
    def setZeroes(self, matrix):

        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # Check first row
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True

        # Check first col
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True

        # Mark rows & cols
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zeroes based on marks
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # First row
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # First col
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0