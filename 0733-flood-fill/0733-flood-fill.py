class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nr, nc = len(image), len(image[0])
        sv = image[sr][sc]
        
        if sv == color:
            return image
        
        def dfs(r, c):
            if image[r][c] == sv:
                image[r][c] = color
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < nr:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < nc:
                    dfs(r, c + 1)
                    
        dfs(sr, sc)
        return image
        
            