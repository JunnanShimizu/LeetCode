class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False

        stack = []
        closeToOpen = {'}' : '{', ')' : '(', ']' : '['}

        for c in s:
            if c in closeToOpen: # if c is a closing character
                if stack and (stack[-1] == closeToOpen[c]): # if the stack in not empty and the last added value is equal to its key/value pair
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False