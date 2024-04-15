class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for char in s:
            if char.isalnum():
                string.append(char)
        top = len(string) - 1

        for i in range(len(string)):
            if string[i].lower() != string[top].lower():
                return False
            top -= 1
            if top < i:
                break

        return True

