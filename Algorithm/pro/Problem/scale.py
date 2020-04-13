# 저울
'''
! 아이디어 떠올리는게 어렵다

Reference: https://gurumee92.tistory.com/185


입출력 예
weight	return
[3, 1, 6, 2, 7, 30, 1]	21
'''


def solution(weight):
    answer = 1
    
    for w in sorted(weight):
        if answer >= w:
            answer += w
        
    return answer


weight = [3, 1, 6, 2, 7, 30, 1]
print(solution(weight))