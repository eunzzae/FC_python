# stack 문제
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        } 
        
        for i in pares : 
            if i in parentheses.keys():
                stack.append(i)
            elif (not stack) or (parentheses[stack.pop()] != i):
                
                return False
        return len(stack) == 0

