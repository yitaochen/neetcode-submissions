class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use the trick index = i * n + j
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            i = mid // n
            j = mid % n 
            if matrix[i][j] > target:
                r -= 1
            elif matrix[i][j] < target:
                l += 1
            else:
                return True 
        
        return False
