# 백준 1439번 뒤집기
# https://www.acmicpc.net/problem/1439
'''
a -> b 뒤집기
'0' -> '1'
'1' -> '0'
각각의 경우를 해보고 두 경우 중 가장 적은 뒤집기 횟수를 출력

test case
0001100
'''

def func(s, a, b):
    lst = s[::]
    res = 0
    for i in range(len(lst)):
        if lst[i] == a:
            lst[i] = b
            for j in range(i+1, len(lst)):
                if lst[j] == a:
                    lst[j] = b
                else:
                    break
            res += 1
    return res


s = list(input())
result = min(func(s, '1', '0'), func(s, '0', '1'))
print(result)



# 다른 사람 풀이 !!
'''
규칙을 발견

0/1 -> 0
01/10 -> 1
010/101 -> 1
1010/0101 -> 2
...

뒤집는 횟수 = (값이 바뀌는 구간의 개수 + 1) // 2
'''

S, tot = input(), 0
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        tot += 1

print((tot + 1) // 2)
