# 백준 1874번 스택 수열
# https://www.acmicpc.net/problem/1874
'''

n=8일때,
[1, 2, 3, 4, 5, 6, 7, 8]을 [4, 3, 6, 8, 7 ,5, 2, 1]로 push 와 pop를 이용해서 만들때
push이면 '+'를 pop이면 '-'를 출력
'''

# 나중에 다시 풀어보기!


# 다른 사람 코드
n = int(input())

cnt = 1
stack = []
res = []

for i in range(1, n+1):
    data = int(input())
    
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        res.append("+")
    
    if stack[-1] == data:
        stack.pop()
        res.append("-")
    else:
        print("NO")
        exit(0)

print('\n'.join(res))