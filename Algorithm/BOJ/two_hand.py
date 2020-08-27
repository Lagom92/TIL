# 백준 16675번 두 개의 손
# https://www.acmicpc.net/problem/16675
'''
한쪽이 같은 걸 냈을때만 승부를 알 수 있다.
그 외의 경우에는 ? 
'''

m1, m2, t1, t2 = list( 'SPR'.index(i) for i in input().split())

print(m1, m2, t1, t2)

if m1 == m2 and (m1 + 2)%3 in [t1, t2]:
        print("TK")
elif t1 == t2 and (t1 + 2)%3 in [m1, m2]:
        print("MS")
else:
    print("?")