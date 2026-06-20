class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        openSymbols = {'(' : ')', '{' : '}', '[': ']'}
        stack = []
        for char in s:
            if char in openSymbols:
                stack.append(openSymbols[char])
            else:
                if not stack: return False
                truth = stack.pop()
                if char != truth: return False
        if stack: return False
        return True
