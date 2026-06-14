class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        seen = [[0] * n for _ in range(m)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(i, j, l, seen):
            if l == len(word) - 1 and board[i][j] == word[l]:
                return True
            if board[i][j] != word[l]:
                return False
            seen[i][j] = 1
            flag = False
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not seen[ni][nj]:
                    flag |= dfs(ni, nj, l+1, seen)
            seen[i][j] = 0

            return flag

        return any(dfs(i, j, 0, seen) for i in range(m) for j in range(n))

            

