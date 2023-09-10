# strand1과 strand2 사이의 해밍 거리 반환
# strand1과 strand2의 길이는 동일
def distance(strand1, strand2):
    distance = 0
    L = len(strand1)
    for i in range(L):
        if strand1[i] != strand2[i] :
            distance += 1
    # 차이의 갯수 반환
    return distance

# 두 가닥의 길이가 동일하지 않을 경우, 에러를 발생시켜야 합니다.
raise ValueError("Strands must be of equal length.")