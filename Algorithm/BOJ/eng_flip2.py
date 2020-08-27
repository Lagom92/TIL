# 백준 17413번 단어 뒤집기2
# https://www.acmicpc.net/problem/17413
'''
text에서 값을 하나씩 꺼내면서 비교하면서 진행

< 나오면 > 가 나올때까지 while
re_word에는 값을 거꾸로 넣기
" "이 나오면 모아둔 re_word를 res에 더하기
'''

text = [i for i in input()]

res = ""
re_word = ""
while text:
    t = text.pop(0)
    if t == '<':
        if len(re_word):
            res += re_word
            re_word = ""
        while True:
            res += t
            t = text.pop(0)
            if t == '>':
                res += t
                break
    else:
        if t == " ":
            res += re_word + " "
            re_word = ""
        else:
            re_word = t + re_word
    
print(res + re_word)



# 다른 사람 코드
'''
시간 차이가 엄청 난다...

조건을 잘 설정해야함
'''
S = input()

tmp, ans, ck = '', '', False

for i in S:
    if i == ' ':
        if not ck:
            ans += tmp[::-1] + ' '
            tmp = ''
        else:
            ans += ' '
    elif i == '<':
        ck = True
        ans += tmp[::-1] + '<'
        tmp = ''
    elif i == '>':
        ck = False
        ans += '>'
    else:
        if ck:
            ans += i
        else:
            tmp += i
ans += tmp[::-1]

print(ans)
