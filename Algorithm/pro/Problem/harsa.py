# 하샤드 수
'''
- 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.

몫이 0이 아닐때 까지 while문을 진행
나머지를 num에 모음
나누어 떨어지는지 확인하여 리턴(True/False)


입출력 예
arr	return
10	true
12	true
11	false
13	false
'''



def solution(x):
    init_x = x
    num = 0
    while x//1:
        num += (x%10)
        x //= 10

    return (False if init_x%num else True)


x = 13
print(solution(x))



# 다른사람 코드
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

print(Harshad(18))  # True 


'''

출력이 True/False 이므로 관계연산자를 이용해 출력한것이 좋아보임

'''