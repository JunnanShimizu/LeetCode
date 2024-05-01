class Solution {
public:
    int reverse(int x) {
        bool isNegative = false;
        long xl = x;
        if(x < 0){
            isNegative = true;
            xl *= -1;
        }
        
        std::string strX = std::to_string(xl);
        std::string newString = "";
        for(int i = strX.length() - 1; i >= 0; i--){
            newString += strX[i];
        }
        
        if(isNegative){
            newString = "-" + newString;
        }
        
        if(std::stol(newString) > std::pow(2, 31) + 1 || std::stol(newString) < std::pow(-2, 31)){
            return 0;
        }else{
            return std::stoi(newString);
        }
    }
};