class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        return_chars = ['}', ')', ']']
        for char in s:
            if return_chars.count(char):
                if not stack:
                    return False
                if char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif char == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(char)
        if not stack:
            return True
        return False