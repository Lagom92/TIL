# 백준 10989번 수 정렬하기3
# https://www.acmicpc.net/problem/10989
'''
N개의 수가 주어질때, 오름차순으로 정렬하기
'''
# test case는 통과함 but 메모리 초과 발생함
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()

for i in numbers:
    print(i)



'''
dict를 사용해서 key에 숫자, value에 횟수를 저장했다.
그런데 시간초과가 발생함

알고보니 input()을 사용하면 느려서 시간초과가 발생할 수 있음

import sys
sys.stdin.readline()

을 사용하면 시간초과 문제가 해결됨
'''
import sys

N = int(sys.stdin.readline())
numbers = {}
for _ in range(N):
    data = int(sys.stdin.readline())
    if data in numbers:
        numbers[data] += 1
    else:
        numbers[data] = 1

for i in sorted(numbers.keys()):
    for _ in range(numbers[i]):
        print(i)



# 다른 사람 코드
# 리스트의 인덱스를 사용
import sys
N = int(sys.stdin.readline())
numbers = [0] * 10001

for _ in range(N):
    data = int(sys.stdin.readline())
    numbers[data] += 1

for idx, i in enumerate(numbers):
    if i != 0:
        for _ in range(i):
            print(idx)
            