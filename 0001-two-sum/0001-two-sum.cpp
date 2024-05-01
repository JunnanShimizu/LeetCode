class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i1 = 0; i1 < nums.size(); i1++){
            for(int i2 = 0; i2 < nums.size(); i2++){
                if(i1 == i2){
                   continue;
                } else {
                    if(nums[i1] + nums[i2] == target){
                        return {i1, i2};
                    }
                }
            }
        }
        
        return {};
    }
};