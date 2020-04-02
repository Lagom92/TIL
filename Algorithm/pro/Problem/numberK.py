# k번째 수
'''
commands를 for문으로 돌면서 
슬라이싱(index 주의!)
정렬(sort)
k번째 숫자를 answer에 넣기(index 주의!)

answer 출력
'''
'''
array	commands	return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
'''


def solution(array, commands):
    answer = []
    for c in commands:
        box = array[c[0]-1:c[1]]
        box.sort()
        answer.append(box[c[2]-1])
    
    return answer



# 다른사람 코드1
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))



# 다른사람 코드2
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer