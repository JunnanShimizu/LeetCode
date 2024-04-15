class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        
        mvol = 0
        l, r = 0, len(height) - 1

        while l < r:
            vol = min(height[l], height[r]) * (r - l)
            if vol > mvol:
                mvol = vol
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return mvol