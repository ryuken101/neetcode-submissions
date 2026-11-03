class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedtoopen = {")": "(", "}": "{", "]": "["}
        for char in s: 
            if char in closedtoopen: 
                if stack and stack[-1] == closedtoopen[char]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(char)
        if not stack: 
            return True
        else: 
            return False
        