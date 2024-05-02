class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        red = 0
        white = 0
        blue = 0
        
        for n in nums:
            if n == 0:
                red += 1
            if n == 1:
                white += 1
            if n == 2:
                blue += 1
        
        index = 0
        for n in range(red):
            nums[index] = 0
            index += 1
            
        for n in range(white):
            nums[index] = 1
            index += 1
            
        for n in range(blue):
            nums[index] = 2
            index += 1
                