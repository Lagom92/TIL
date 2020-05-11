# 백준 2747번 피보나치 수
# https://www.acmicpc.net/problem/2747
'''
피보나치 수: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
'''
# test case는 통과하지만 시간 초과 발생함
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)



# list를 이용(DP)
n = int(input())
box = [0, 1] + [0] * (n-1)

for i in range(2, n+1):
    box[i] = box[i-1] + box[i-2]

print(box[-1])



# 다른 사람 코드
n = int(input())
a, b = 0, 1

while n > 0:
    a, b = b, a+b
    n -= 1

print(a)