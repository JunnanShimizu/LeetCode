class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(on, cn):
            if on == cn == n:
                res.append("".join(stack))
                return
            if on < n:
                stack.append("(")
                backtrack(on + 1, cn)
                stack.pop()
            if cn < on:
                stack.append(")")
                backtrack(on, cn + 1)
                stack.pop()

        backtrack(0, 0)
        return res
            
                