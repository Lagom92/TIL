# 프로그래머스 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993#fnref1
'''

14개 중 8개 맞춤

이유가 머지...??
'''

def solution(skill, skill_trees):
    res = 0
    lst = list(skill)
    for tree in skill_trees:
        box = ""
        # print(tree)
        for t in tree:
            # print(t)
            if t in lst:
                # print(box)
                box += t
        if len(box):
            if box[0] == lst[0]:
                print(box)
                res += 1
        else:
            res += 1

    return res


skill = "CBD"
# skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "CXF", "ASF", "BDF", "CEFD"]
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# res = 2

res = solution(skill, skill_trees)
print(res)
