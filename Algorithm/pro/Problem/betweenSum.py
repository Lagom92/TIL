# 두 정수 사이의 합
'''
a와 b사이의 대소 관계를 생각해서 
a < b 관계가 되게 함

range를 이용해서 숫자들을 만들고 sum()함수로 합을 구함


입출력 예
a	b	return
3	5	12
3	3	3
5	3	12
'''


def solution(a, b):
    if a > b:
        a, b = b, a

    return sum(list(range(a, b+1)))



a = 3
b = 5
res = solution(a, b)
print(res)

# 다른사람 코드1
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2


# 다른사람 코드2
def adder(a, b):
    # 함수를 완성하세요
    return sum(range(min(a,b),max(a,b)+1))