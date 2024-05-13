class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        int count = 0;
        int location = 0;
        
        for(int i = 0; i < nums.size(); i++){
            location += nums[i];
            if(location == 0){
                count += 1;
            }
        }
        
        return count;
    }
};