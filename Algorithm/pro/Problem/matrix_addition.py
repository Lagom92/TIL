# 프로그래머스 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950
'''
test case
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]
'''

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        res = []
        for j in range(len(arr1[i])):
            res.append(arr1[i][j] + arr2[i][j])
        answer.append(res)
    return answer



# 다른사람 코드 1
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))


# 다른사람 코드 2
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A


# 다른사람 코드 3
import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()