// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        for(int i = 1; i <= n; i++){
            bool isBad = isBadVersion(i);
            if(isBad){
                return i;
            }
        }
        return -1;
    }
};