def solution(s):
    mapping_table = { 
            "(" : ")",
            "[" : "]",
            "{" : "}"}
    
    stack = []
    for p in s : 
        if p == "(" or p == "{" or p == "[":
            stack.append(p)
        elif p != mapping_table[stack[-1]]:
            return False
        elif p == mapping_table[stack[-1]]:
            stack.pop()
    return not stack

print(solution(s = "(()[]{}" ))