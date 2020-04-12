# 콜라츠 추측
'''
1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

입출력 예
n	result
6	8
16	4
626331	-1
'''


def solution(num):
    cnt = 0

    while num>1:
        cnt += 1
        num = (num*3 + 1) if num%2 else (num // 2)
        
        if cnt > 500:
            return -1

    return cnt


n = 6
print(solution(n))