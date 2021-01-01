# 프로그래머스 가장 긴 팰린드롬
# https://programmers.co.kr/learn/courses/30/lessons/12904


'''
효율성 실패

정확성: 69.3
효율성: 0.0
합계: 69.3 / 100.0
'''
def solution(s):
    answer = 0
    n = len(s)
    for i in range(0, n):
        for j in range(1, n+i+1):
            sub = s[i:i+j]
            if sub == sub[::-1]:
                if answer <= len(sub):
                    answer = len(sub)
    return answer

s = "토마토맛토마토"    # ans=7
ans = solution(s)
print(ans)


# 다른 사람 코드
def longest_palindrom(s):
    for i in range(len(s),0,-1):  # 큰 길이 -> 작은 길이
        for j in range(len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:  # 팰린드롬이라면 
                return i

s = "abacde"
print(longest_palindrom(s))
