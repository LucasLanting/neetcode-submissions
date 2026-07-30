class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # if the stack is empty add the character to the stack
            if not stack:
                stack.append(char)
                continue
            left_bracket = stack[-1]
            if left_bracket == '[' and char == ']':
                stack.pop()
            elif left_bracket == '{' and char == '}':
                stack.pop()
            elif left_bracket == '(' and char == ')':
                stack.pop()
            else:
                stack.append(char)
        return  not stack