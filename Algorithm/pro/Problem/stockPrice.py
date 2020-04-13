# 주식가격
'''
문제 설명이 좀 이상함

가격이 떨어질때 까지 걸리는 시간을 구하는 문제


입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
'''

# 1's 코드
# 정확성 테스트 합격, 효율성 테스트 불합격
def solution(prices):
    answer = []

    while prices:
        price = prices.pop(0)

        flag = True
        for i in range(len(prices)):
            if price > prices[i]:
                answer.append(i+1)
                flag = False
                break

        if flag:
            answer.append(len(prices))
        
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
