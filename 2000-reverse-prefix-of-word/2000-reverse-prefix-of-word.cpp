class Solution {
public:
    string reversePrefix(string word, char ch) {
        int index = word.find(ch);
        
        if(index == std::string::npos){
            return word;
        }
        
        string newString = "";
        for(int i = index; i >= 0; i--){
            newString += word[i];
        }
        
        return newString + word.substr(index + 1);
    }
};