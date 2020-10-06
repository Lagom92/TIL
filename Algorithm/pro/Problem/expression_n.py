# 프로그래머스 N으로 표현
# https://programmers.co.kr/learn/courses/30/lessons/42895
'''

입출력 예
N	number	return
5	12	4
2	11	3
'''

def func(n, number):
    res = []
    for i in range(1, 9):
        set_data = set()
        set_data.add(int(str(n)*i))

        for j in range(0, i - 1):
            for x in res[j]:
                for y in res[-j - 1]:
                    set_data.add(x + y)
                    set_data.add(x - y)
                    set_data.add(x * y)
                    if y:
                        set_data.add(x // y)

        res.append(set_data)

        if number in set_data:
            return i
    return -1

# n = int(input())
# number = int(input())

# print(func(n, number))
print(func(4,17),4)



# 다른 사람 코드
def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        num_set = { int(str(N) * i) }

        for j in range(0, i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    num_set.add(x + y)
                    num_set.add(x - y)
                    num_set.add(x * y)

                    if y != 0:
                        num_set.add(x // y)

        if number in num_set:
            return i

        DP.append(num_set)

    return answer

print(solution(4,17),4)