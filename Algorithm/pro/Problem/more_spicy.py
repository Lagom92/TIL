# 더 맵게
'''

입출력 예
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
'''


'''
1's code
정확성 합격, 효율성 탈락
'''
def solution1(scoville, K):
    cnt = 0
    while True:
        scoville.sort()

        if scoville[0] >= K:
            return cnt

        if len(scoville) == 1:
            return -1

        cnt += 1
        not_spicy1 = scoville.pop(0)
        not_spicy2 = scoville.pop(0)
        mix_spicy = not_spicy1 + (not_spicy2*2)
        scoville.append(mix_spicy)

    return cnt



scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))