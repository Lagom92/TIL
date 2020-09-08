# 프로그래머스 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163
'''
조건
1. 한 번에 한 개의 알파벳만 변경
2. words에 있는 단어로만 변경
'''
import copy

# 두 단어를 비교해서 변경 가능한지 체크하는 함수
def change_word(val, word):
    cnt = 0
    for i in range(len(word)):
        if val[i] == word[i]:
            cnt += 1
        
    if len(word) - cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0
    box = []
    q = []
    box.append(begin)
    visited = [0]*len(words)

    while box:
        if target in box:
            return answer

        val = box.pop(0)

        for word in words:
            if change_word(val, word):
                if visited[words.index(word)] == 0:
                    visited[words.index(word)] = 1
                    q.append(word)
        if len(box) == 0:
            box = copy.deepcopy(q)
            q = []
            answer += 1

    return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["hot", "dot", "dog", "lot", "log"]


res = solution(begin, target, words)
print(res)
