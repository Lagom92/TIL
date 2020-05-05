# 백준 2798번 블랙잭

import itertools

def blackjack(N, M, num_cards):
    maxV = 0
    sum_cards = list(itertools.combinations(num_cards, 3))
    for card in sum_cards:
        if maxV <= sum(card) <= M:
            maxV = sum(card)

    return maxV

N, M = map(int, input().split())
num_cards = list(map(int, input().split()))

res = blackjack(N, M, num_cards)
print(res)




# 남의 코드
n, m = list(map(int, input().split()))
data = list(map(int, input().split()))

result = 0
length = len(data)

count = 0
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)