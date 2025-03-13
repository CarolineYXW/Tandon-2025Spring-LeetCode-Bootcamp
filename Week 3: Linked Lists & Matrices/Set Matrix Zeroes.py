class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row1_0 = col1_0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                col1_0 = True
        for j in range(n):
            if matrix[0][j] == 0:
                row1_0 = True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if row1_0:
            for j in range(n):
                matrix[0][j] = 0
        if col1_0:
            for i in range(m):
                matrix[i][0] = 0