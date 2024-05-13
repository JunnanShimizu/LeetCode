class Solution {
    public int returnToBoundaryCount(int[] nums) {
        int count = 0;
        int location = 0;
        
        for(int i = 0; i < nums.length; i++){
            location += nums[i];
            if(location == 0)
                count++;
        }
        
        return count;
    }
}