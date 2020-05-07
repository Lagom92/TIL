# 백준 5397번 키로거
# https://www.acmicpc.net/problem/5397
'''
test case

2
<<BP<A>>Cd-
ThIsIsS3Cr3t

'''

# test case는 통과함, 런타임 에러 발생함, 이유 모르겠음

T = int(input())
for _ in range(T):
    keylogger = input()
    cursor = 0
    password = []

    for log in keylogger:
        if log == "<" and cursor > 0:
            cursor -= 1
        elif log == ">" and cursor < len(password):
            cursor += 1
        elif log == "-":
            password.pop(cursor-1)
        else:
            password.insert(cursor, log)
            cursor += 1

    print(''.join(password))



# 다른 사람 코드
'''
2개의 스택(left, right)을 이용
<: left의 원소를 right로 이동
>: right의 원소를 left로 이동
-: left에 값이 있을 경우, 원소를 하나 제거
'''
tc = int(input())

for _ in range(tc):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == "-":
            if left_stack:
                left_stack.pop()
        elif i == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))