# 백준 1966번 프린터 큐
# https://www.acmicpc.net/problem/1966


T = int(input())
for tc in range(T):
    N, M = list(map(int, input().split()))
    docs = list(map(int, input().split()))

    docs_idx = [ _ for _ in range(N)]
    maxV = max(docs)
    cnt = 1

    while docs:
        doc = docs.pop(0)
        idx = docs_idx.pop(0)
        if doc == maxV and idx == M:
            print(cnt)
            break

        if maxV == doc:
            cnt += 1
            maxV = max(docs)
        else:
            docs.append(doc)
            docs_idx.append(idx)




# 다른 사람 코드
tc = int(input())

for _ in range(tc):
    n, m = list(map(int, input().split()))
    que = list(map(int, input().split()))
    # enumerate를 이용해서 키와 값을 동시에 사용함
    que = [(i, idx) for idx, i in enumerate(que)]

    count = 0
    while True:
        # max에 key를 이용해서 que의 값 중 최대를 찾음
        if que[0][0] == max(que, key=lambda x: x[0])[0]:
            count += 1
            if que[0][1] == m:
                print(count)
                break
            else:
                que.pop(0)
        else:
            que.append(que.pop(0))