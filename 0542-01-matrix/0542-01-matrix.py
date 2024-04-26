class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    continue
                else:
                    if r > 0:
                        top = mat[r - 1][c]
                    else:
                        top = float('inf')
                    if c > 0:
                        left = mat[r][c - 1]
                    else:
                        left = float('inf')
                    mat[r][c] = min(top, left) + 1
                        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] == 0:
                    continue
                else:
                    if r + 1 < m:
                        bot = min(mat[r][c], mat[r + 1][c])
                    else:
                        bot = float('inf')
                    if c + 1 < n:
                        right = min(mat[r][c], mat[r][c + 1])
                    else:
                        right = float('inf')
                    mat[r][c] = min(mat[r][c], bot + 1, right + 1)
        
        return mat            