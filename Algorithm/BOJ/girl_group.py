# 백준 16165번 걸그룹 마스터 준석이
# https://www.acmicpc.net/problem/16165

N, M = map(int, input().split())
girl_group = {}

# 걸그룹 이름 사전만들기
for _ in range(N):
    team = input()
    girl_group[team] = []
    cnt = int(input())
    for _ in range(cnt):
        member = input()
        girl_group[team].append(member)

# 퀴즈 풀기
for _ in range(M):
    problem = input()
    kind = int(input())

    if kind:    # 퀴즈 종류 = 1, 해당 멤버가 속한 팀의 이름 출력
        for girl in girl_group:
            if problem in girl_group[girl]:
                print(girl)
                break
    else:       # 퀴즈 종류 = 0, 해당 팀에 속한 멤버의 이름 출력(사전순)
        for girl in sorted(girl_group[problem]):
            print(girl)
