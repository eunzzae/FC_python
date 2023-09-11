# stack 문제
def Solution(s):
        stack = []
        parentheses = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        } 
        
        for i in s : 
            if i in parentheses.keys():
                stack.append(i)
            elif (not stack) or (parentheses[stack.pop()] != i):
                
                return False
        return len(stack) == 0

print(Solution(s = "(()[]{}" ))