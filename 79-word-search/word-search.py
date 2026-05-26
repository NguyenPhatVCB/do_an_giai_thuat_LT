class Solution:
    def exist(self, board, word):

        m, n = len(board), len(board[0])
        visited = set()

        def dfs(i, j, k):

            if k == len(word):
                return True

            if (i < 0 or i >= m or j < 0 or j >= n or
                (i, j) in visited or board[i][j] != word[k]):
                return False

            visited.add((i, j))

            res = (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )

            visited.remove((i, j))

            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False