# 백준 1427번 소트인사이드
# https://www.acmicpc.net/problem/1427
'''
내림차순으로 정렬하기
'''
# sort(reverse=True) 사용
nums = list(int(i) for i in input())
nums.sort(reverse=True)
for n in nums:
    print(n, end='')




# 다른 사람 코드
'''
9 ~ 0까지 순회하면서 array에 해당 숫자가 있으면 출력
'''
array = input()

for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end='')