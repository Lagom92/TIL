# 프로그래머스 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993#fnref1
'''

미완
'''


def solution(skill, skill_trees):
    res = 0
    for skill_tree in skill_trees:
        box = list(skill)
        i = 0
        while skill_tree:
            t = skill_tree.pop(0)
            if i < len(box):
                if t == box[i]:
                    i += 1
                else:
                    if t in box:
                        idx = box.index(t)
                        

            else:
                pass
            


            else:
                pass
                

            
        




    return res


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# res = 2

res = solution(skill, skill_trees)
print(res)
