# 백준 2480번 주사위 세개
# https://www.acmicpc.net/problem/2480
'''
같은 눈(n)이 3개면 10000 + n*1000
같은 눈(n)이 2개면 1000 + n*100
모두 다른 눈이면 가장큰 눈(n) * 100
'''

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a*1000)
elif a == b:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
elif a == c:
    print(1000 + a*100)
elif a != b != c:
    max_num = max(a, b, c)
    print(max_num*100)



# 다른 사람 코드
# set()을 이용해서 같은 수가 몇개 있는지 확인
lst = sorted(list(map(int, input().split())))

if len(set(lst)) == 1:          # 같은 눈이 3개
    print(10000 + lst[0] * 1000)
elif len(set(lst)) == 2:
    # 정렬된 리스트의 중간에 있는 값이 중복된 값일 것 이다.
    print(1000 + lst[1] * 100)
else:
    print(lst[2] * 100)
