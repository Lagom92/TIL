# S/W 문제해결 기본 1일차 - Flatten
'''
평탄화 작업 후 (최대값 - 최소값) 출력하기

결국 최대와 최소를 찾아서 각각 1을 빼고, 더해주면 됨

최대값, 최소값 찾기
최대값과 최소값의 인덱스 찾기
최대값과 최소값에 -1, +1 하기
위 과정을 dump 횟수만큼 반복하기
'''

for tc in range(1, 2):
    dump = int(input())
    field = list(map(int, input().split()))
    for _ in range(dump):
        minV = min(field)
        maxV = max(field)
        minV_idx = field.index(minV)
        maxV_idx = field.index(maxV)
        field[minV_idx] += 1
        field[maxV_idx] -= 1
    res = max(field) - min(field)

    print(f"#{tc} {res}")




# 다른 사람 코드
for r in range(1, 11):
    dump = int(input())
    boxPos = sorted(list(map(int, input().strip().split())))
     
    while dump > 0:
        boxPos[-1] -= 1
        boxPos[0] += 1
        boxPos.sort()
        dump -= 1
         
    print("#{}".format(r), max(boxPos)-min(boxPos))