# 백준 7490번 0 만들기
# https://www.acmicpc.net/problem/7490
'''
eval(): 문자열로 된 계산식을 계산하는 함수
'''

# test case가 맞긴 한데 출력 순서가 달라서 오답처리가 됨
# 해결방법은 모르겠음
def solution(n, i, expression):
    num_list = [num for num in range(1, n+1)]
    
    if i == n-1:
        if eval(expression.replace(" ", "")) == 0:
            print(expression)
        return
    else:
        solution(n, i+1, expression+ '+' + str(num_list[i+1]))
        solution(n, i+1, expression+ '-' + str(num_list[i+1]))
        solution(n, i+1, expression+ ' ' + str(num_list[i+1]))


T = int(input())
for _ in range(T):
    n = int(input())

    solution(n, 0, '1')

    print()




# 다른 사람 코드
import copy

def func(arr, n):
    if len(arr) == n:
        operator_array.append(copy.deepcopy(arr))
        return
    
    arr.append(" ")
    func(arr, n)
    arr.pop()
    
    arr.append("+")
    func(arr, n)
    arr.pop()
    
    arr.append("-")
    func(arr, n)
    arr.pop()
    
test_case = int(input())

for _ in range(test_case):
    n = int(input())
    operator_array = []
    integer = [i for i in range(1,n+1)]
    
    func([], n-1)
    
    for operator in operator_array:
        total = ""
        
        for i in range(n-1):
            total += str(integer[i]) + operator[i]
        total += str(integer[-1])
        
        if eval(total.replace(" ","")) == 0:
            print(total)
    print()