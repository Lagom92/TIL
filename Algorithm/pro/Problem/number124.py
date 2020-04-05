# 124 나라의 숫자
'''
n = 3 * X + y

몫과 나머지를 사용
인덱스 주의

! 다른사람의 코드를 참고했음, 추후 복습 필요


입출력 예
n	result
1	1
2	2
3	4
4	11
'''



def solution(n):
    num = "124"
    ans = ""
    
    if n < 4:
        return num[n-1]
    
    while n > 0:
        n = n-1
        ans = num[n%3] + ans
        n = n // 3
    
    return ans



# 다른사람 코드_재귀사용
def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]



n = 15
res = solution(n)
print(f"res: {res}")