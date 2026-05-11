class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')':'(', ']':'[', '}':'{'}
        stack = []

        for ch in s:
            if ch not in matches:
                stack.append(ch)
            else:
                if stack and stack[-1] == matches[ch]:
                    stack.pop()
                else:
                    return False
        return not stack
            