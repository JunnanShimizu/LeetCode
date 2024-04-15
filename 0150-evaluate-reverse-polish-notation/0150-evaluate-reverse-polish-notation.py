class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0
        for val in tokens:
            if val == "+":
                stack.append(stack.pop() + stack.pop())
            elif val == "-":
                s = stack.pop()
                f = stack.pop()
                stack.append(f - s)
            elif val == "*":
                stack.append(stack.pop() * stack.pop())
            elif val == "/":
                s = stack.pop()
                f = stack.pop()
                stack.append(int(f / s))
            else:
                stack.append(int(val))
        
        return stack[0]