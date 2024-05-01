class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        std::vector<std::string> words;
        std::stringstream ss(sentence);
        std::string currentWord;
        
        while (ss >> currentWord) {
            words.push_back(currentWord);
        }
        
        std::string newSentence = "";
        for(std::string& word : words){
            for(std::string dictWord : dictionary){
                if(word.substr(0, dictWord.length()) == dictWord){
                    if(dictWord.length() < word.length()){
                        word = dictWord;
                    }
                }
            }
            newSentence += word + " ";
        }
        
        return newSentence.substr(0, newSentence.length() - 1);
    }
};