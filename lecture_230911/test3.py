# stack 문제

# 시간초과 코드
def solution(temperatures):
    n = len(temperatures)
    answer = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if temperatures[i] < temperatures[j]:
                answer[i] = j - i
                break
    return answer 

print(solution(temperatures = [73,74,75,71,69,72,76,73]))

answer = [0, 0, 0, 0, 0, 0, 0]
