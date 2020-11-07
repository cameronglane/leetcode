class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in char_map:
                top = stack.pop() if stack else 'empty'

                if char_map[char] != top:
                    return False
            else:
                stack.append(char)
    
        return not stack

#Alt:
class Solution2:
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