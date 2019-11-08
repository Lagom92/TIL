# BOJ
# 10539번 문제 수빈이와 수열
'''
A -> B 
1, 2 -> 1/1, 1+2/2

B를 이용해서 A구하기
문제 이해 필수!
'''


N = int(input())
B = list(map(int, input().split()))

A = [] # 결과
res = 0     # 전까지의 숫자 합
for i in range(N):
    data = B[i]*(i+1) - res
    res += data
    A.append(data)
print(*A)


'''
다른 풀이 방법 A
'''
print("다른 풀이")
N, B = int(input()), list(map(int, input().split()))

A = [B[0]]

for i in range(1, N):
    A.append(B[i]*(i+1) - sum(A))

print(*A)


'''
다른 풀이 방법 B
'''
print("다른 풀이")
N, B = int(input()), list(map(int, input().split()))

A = [0 for i in range(N)]
A[0] = B[0]

for i in range(1, N):
    A[i] = (B[i]*(i+1) - sum(A))

print(*A)
