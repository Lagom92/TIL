# 기능 개발
'''
배포 날짜 계산
앞 기능 날짜와 뒤 기능 날짜 비교 - 같은 날짜에 배포되도록 날짜를 일치 시킴
for문을 돌면서 같은 날짜의 개수들을 반환

입출력 예
progresses	speeds	return
[93,30,55]	[1,30,5]	[2,1]
'''


import math

def solution(progresses, speeds):
    answer = []
    days = []

    # 배포 가능 날짜 계산
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i]) 
        days.append(day)

    # days=[7, 3, 9] => [7, 7, 9]
    for j in range(len(days)-1):
        if days[j] >= days[j+1]:
            days[j+1] = days[j]
    
    cnt = 1
    for d in range(len(days)-1):
        if days[d] < days[d+1]:
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1

    answer.append(cnt)
            
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))



# 다른 사람 코드 1
def solution1(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


# 다른 사람 코드 2
def solution2(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


print(solution2(progresses, speeds))