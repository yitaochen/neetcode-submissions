class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # rotate cw = flip + transpose
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            for i in range(m//2):
                matrix[i][j], matrix[m-i-1][j] = matrix[m-i-1][j], matrix[i][j]
        
        for i in range(1, m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
