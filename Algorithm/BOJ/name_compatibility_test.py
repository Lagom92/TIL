# 백준 17269번 이름궁합 테스트
# https://www.acmicpc.net/problem/17269


stroke_count = {
    'A':3, 'B':2, 'C':1, 'D':2, 'E':4,
    'F':3, 'G':1, 'H':3, 'I':1, 'J':1,
    'K':3, 'L':1, 'M':3, 'N':2, 'O':1,
    'P':2, 'Q':2, 'R':2, 'S':1, 'T':2,
    'U':1, 'V':1, 'W':1, 'X':2, 'Y':2,
    'Z':1
}

N, M = map(int, input().split())
a_name, b_name = input().split()

AB = ''
lst = list()
minlen = N if N < M else M

# 이름 합치기
for i in range(minlen):
    AB += a_name[i] + b_name[i]
AB += a_name[minlen:] + b_name[minlen:]

# 알파벳을 획수로 바꾸기
for i in AB:
    lst.append(stroke_count[i])

# 획수 더하기(0번과 1번 인덱스로)
for i in range(len(lst)-2):
    for j in range(len(lst)-1-i):
        lst[j] += lst[j+1]
        lst[j] %= 10

res = (lst[0]*10 + lst[1]) % 100
print(f"{res}%")