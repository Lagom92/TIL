# 더 맵게
'''
최소 값을 뽑아서 계산(a+b*2)을 하여 K와 비교


입출력 예
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
'''


'''
1's code
정확성 합격, 효율성 탈락
'''
# def solution1(scoville, K):
#     cnt = 0
#     while True:
#         scoville.sort()

#         if scoville[0] >= K:
#             return cnt

#         if len(scoville) == 1:
#             return -1

#         cnt += 1
#         not_spicy1 = scoville.pop(0)
#         not_spicy2 = scoville.pop(0)
#         mix_spicy = not_spicy1 + (not_spicy2*2)
#         scoville.append(mix_spicy)

#     return cnt



'''
2's 풀이

heapq를 사용하여 해결!


! 길이가 1이라고 무조건 -1을 반환하면 않됨
'''

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        minV1 = heapq.heappop(scoville)

        if minV1 >= K:
            return cnt
        
        try:
            minV2 = heapq.heappop(scoville)
        except:
            return -1
        
        value = minV1 + minV2*2
        cnt += 1

        heapq.heappush(scoville, value)

    return None



scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))