# 완주하지 못한 선수
'''
두 배열을 정렬
해당 인덱스에 같은 이름이 있는지 확인하여
참여자 명단에만 있는 이름 출력

완주자 명단을 다 돌았는데도 
이름을 못 찾으면 참여자 명단 중 마지막 이름을 출력
'''

'''
participant	completion	return
[leo, kiki, eden]	[eden, kiki]	leo
[marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
[mislav, stanko, mislav, ana]	[stanko, ana, mislav]	mislav
'''


def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]


# 다른사람 코드
import collections

def func(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

participant = ["leo", "kiki", "eden"]
completion = ["kiki", "eden"]
result = func(participant, completion)
print(result)
