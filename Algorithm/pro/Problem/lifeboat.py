# 구명 보트
'''
숫자(x)를 하나 뽑은 후
limit - x 보다 작은 수 중에서 가장 큰 수를 제거하고 cnt += 1
 

입출력 예
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3

hidden testcase
people = [10,20,30,40,50,60,70,80,90]
limit = 100
return = 5
'''


'''
1's code

정확도 pass / 효율성 fail
'''
def solution1(people, limit):
    people.sort(reverse=True)
    cnt = 0
    while people:
        p1 = people.pop()
        if people:
            for i, man in enumerate(people):
                if p1 + man <= limit:
                    people.pop(i)
                    break
        
        cnt += 1
        
    return cnt



people = [70, 80, 50]
limit = 100

print(solution1(people, limit))